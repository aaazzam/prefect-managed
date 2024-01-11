from prefect import flow


@flow(log_prints=True)
def buy():
    print("Selling securities")


if __name__ == "__main__":
    flow.from_source(
        "https://github.com/aaazzam/prefect-managed.git",
        entrypoint="test.py:buy",
    ).deploy(
        name="prefect-managed-2", interval=60, work_pool_name="Managed Pool", push=False
    )
