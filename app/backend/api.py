from backend.db.engine import async_session_maker, create_all_tables
from backend.models.wallets import WalletModel
from backend.schemas.wallet import WalletRequest
from backend.schemas.response import SimpleResponse

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.engine import ScalarResult


router = APIRouter(prefix="/api/v1")


@router.get("/check_eligibility")
async def check_eligibility(wallet: WalletRequest):
    async with async_session_maker() as session:
        res: ScalarResult = await session.execute(
            select(WalletModel).where(WalletModel.address == wallet.address)
        )
        current_wallet: WalletModel = res.scalars().one_or_none()
        if current_wallet:
            return SimpleResponse(response="eligible")
        return SimpleResponse(response="isnt_eligible")
