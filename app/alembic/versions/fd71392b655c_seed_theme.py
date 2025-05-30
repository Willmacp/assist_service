"""add_theme_use_case_data

Revision ID: fd71392b655c
Revises: c732af2e465a
Create Date: 2024-04-08 10:29:37.645034

"""

from collections.abc import Sequence

from alembic import op
from sqlalchemy import MetaData, Table

# revision identifiers, used by Alembic.
revision: str = "fd71392b655c"
down_revision: str | None = "c732af2e465a"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    meta = MetaData()
    meta.reflect(bind=op.get_bind())
    theme_table = Table("theme", meta)
    op.bulk_insert(
        theme_table,
        [
            {
                "title": "Planning campaigns and communication",
                "subtitle": "Create OASIS plans, design narratives, conduct COM-B analysis",
            },
            {
                "title": "Campaign evaluation",
                "subtitle": "Build theories of change, define outcomes, produce KPIs",
            },
            {
                "title": "Developing marketing and communication content",
                "subtitle": "Design messaging, conduct message testing, summarise text",
            },
            {
                "title": "Media handling and press releases",
                "subtitle": "Brainstorm media questions, write press releases, draft briefings",
            },
            {
                "title": "Exploring strategy risks",
                "subtitle": "Analyse risks, explore consequences, test adversarial strategies",
            },
            {
                "title": "Crisis Communications",
                "subtitle": "Develop response strategies, draft crisis messages",
            },
            {
                "title": "Stakeholder identification and management",
                "subtitle": "Identify stakeholders, understand key requirements",
            },
            {
                "title": "Internal communications",
                "subtitle": "Brainstorm ideas, develop strategies, produce materials",
            },
            {
                "title": "Skills and training",
                "subtitle": "Develop training content, design workshops, optimise text",
            },
            {
                "title": "Inclusive and accessible communications",
                "subtitle": "Considerations, test material for accessibility",
            },
            {
                "title": "Brainstorming and ideation",
                "subtitle": "Consider problems, brainstorm, understand communications impact",
            },
            {
                "title": "Research",
                "subtitle": "Write surveys, create guides, design activities",
            },
            {
                "title": "Recruitment",
                "subtitle": "Test, adapt job descriptions for audiences",
            },
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    meta = MetaData()
    meta.reflect(bind=op.get_bind())
    theme_table = Table("theme", meta)
    d = theme_table.delete().where(theme_table.c.id >= 1)
    op.execute(d)
    # ### end Alembic commands ###
