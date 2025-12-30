from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import timedelta

from database import get_db
from models.apiUsageModel import APIUsage
from utils.security import get_current_user
from utils.rate_APi import RATE_LIMITS, RATE_LIMIT_WINDOW_SECONDS


def rate_limiter(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    method = request.method
    endpoint = request.url.path

    limit = RATE_LIMITS.get(method)
    if not limit:
        return

    window_start = func.now() - timedelta(seconds=RATE_LIMIT_WINDOW_SECONDS)

    recent_count = (
        db.query(func.count(APIUsage.id))
        .filter(
            APIUsage.user_id == current_user.id,
            APIUsage.method == method,
            APIUsage.endpoint == endpoint,
            APIUsage.timestamp >= window_start,
        )
        .scalar()
    )

    if recent_count >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded: {limit} requests per {RATE_LIMIT_WINDOW_SECONDS} seconds",
        )

    db.add(
        APIUsage(
            user_id=current_user.id,
            endpoint=endpoint,
            method=method,
        )
    )
    db.commit()
