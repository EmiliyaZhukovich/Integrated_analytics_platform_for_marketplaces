"""Seed mock data into database."""

import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import AsyncSessionLocal, engine
from app.models import Category, Product, Order, Campaign
from mock_data.generator import generate_all_data


async def seed_database() -> None:
    """Seed mock data into the database."""

    # Generate all mock data
    data = generate_all_data(num_products=100, num_orders=500, num_campaigns=150)

    async with AsyncSessionLocal() as session:
        print("\nInserting categories...")
        categories = []
        for cat_data in data["categories"]:
            cat = Category(name=cat_data["name"], slug=cat_data["slug"])
            session.add(cat)
            categories.append(cat)

        await session.flush()
        print(f"✓ Inserted {len(categories)} categories")

        # Create category mapping
        category_map = {cat.slug: cat.id for cat in categories}

        print("\nInserting products...")
        products = []
        for prod_data in data["products"]:
            prod = Product(
                name=prod_data["name"],
                category_id=category_map[prod_data["category_id"]],
                price=prod_data["price"],
                stock=prod_data["stock"],
            )
            session.add(prod)
            products.append(prod)

        await session.flush()
        print(f"✓ Inserted {len(products)} products")

        # Create product ID mapping
        product_map = {i: prod.id for i, prod in enumerate(products)}

        print("\nInserting orders...")
        orders = []
        for i, order_data in enumerate(data["orders"]):
            # Map product index to actual product ID
            product_id = product_map.get(order_data["product_id"] % len(products))

            order = Order(
                product_id=product_id,
                quantity=order_data["quantity"],
                total_price=order_data["total_price"],
                order_date=order_data["order_date"],
                marketplace=order_data["marketplace"],
            )
            session.add(order)
            orders.append(order)

        await session.flush()
        print(f"✓ Inserted {len(orders)} orders")

        print("\nInserting campaigns...")
        campaigns = []
        for i, campaign_data in enumerate(data["campaigns"]):
            # Map product index to actual product ID
            product_id = product_map.get(campaign_data["product_id"] % len(products))

            campaign = Campaign(
                product_id=product_id,
                platform=campaign_data["platform"],
                budget=campaign_data["budget"],
                impressions=campaign_data["impressions"],
                clicks=campaign_data["clicks"],
                conversions=campaign_data["conversions"],
            )
            session.add(campaign)
            campaigns.append(campaign)

        await session.flush()
        print(f"✓ Inserted {len(campaigns)} campaigns")

        # Commit all changes
        await session.commit()
        print("\n✓ All mock data seeded successfully!")


async def main() -> None:
    """Main entry point."""
    try:
        await seed_database()
    except Exception as e:
        print(f"Error seeding database: {e}")
        raise
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
