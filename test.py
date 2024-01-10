from prefect import flow
from prefect.deployments import DeploymentImage


@flow(log_prints=True)
def buy():
    print("Selling securities")


if __name__ == "__main__":
    buy.deploy(
        name="my-custom-dockerfile-deployment",
        work_pool_name="Managed Pool", 
        image='prefecthq/prefect:2-latest',
    push=False
)





