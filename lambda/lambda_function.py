
import json
import logging
import random
from tenacity import retry, stop_after_attempt, wait_exponential, RetryError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def process_event(event):
    # Simulate random failure
    if random.choice([True, False]):
        raise Exception("Simulated failure during event processing.")
    logger.info("Successfully processed event: %s", json.dumps(event))

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))
    try:
        process_event(event)
        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }
    except RetryError as e:
        logger.error("Event processing failed after retries: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Failed after retries')
        }
