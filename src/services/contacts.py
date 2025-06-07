from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas.schemas import ContactBase

from typing import Self


class ContactService:
    def __init__(self: Self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self: Self, body: ContactBase):
        return await self.repository.create_contact(body)

    async def get_contacts(
        self: Self,
        skip: int,
        limit: int,
        name: str | None,
        surname: str | None,
        email: str | None,
    ):
        return await self.repository.get_contacts(skip, limit, name, surname, email)

    async def get_contact_by_id(self: Self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def update_contact(self: Self, contact_id: int, body: ContactBase):
        return await self.repository.update_contact(contact_id, body)

    async def delete_contact(self: Self, contact_id: int):
        return await self.repository.delete_contact(contact_id)

    async def birthdays(self: Self, skip: int, limit: int):
        return await self.repository.birthdays(skip, limit)
