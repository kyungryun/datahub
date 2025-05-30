from datahub.metadata.urns import DatasetUrn
from datahub.sdk.main_client import DataHubClient

client = DataHubClient.from_env()


client.lineage.add_dataset_transform_lineage(
    upstream=DatasetUrn(platform="snowflake", name="source_table"),
    downstream=DatasetUrn(platform="snowflake", name="target_table"),
    column_lineage={
        "customer_id": ["id"],
        "full_name": ["first_name", "last_name"],
    },
)
# column_lineage is optional -- if not provided, table-level lineage is inferred.
