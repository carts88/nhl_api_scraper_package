import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nhl_api")

def fetch_nhl_api(url, params=None):
    """
    Fetch from NHL records API with decent error handling
    """

    try:
        response = requests.get(
            url,
            params=params,
            headers={"Accept": "application/json"},
            timeout=10          # still keeping a timeout — 10s is usually plenty
        )
        response.raise_for_status()
        return response.json()

    except requests.Timeout:
        logger.error(f"Timeout after 10s: {url}")
        raise

    except requests.ConnectionError:
        logger.error(f"Connection failed: {url}")
        raise

    except requests.HTTPError as e:
        status = e.response.status_code
        try:
            error_detail = e.response.json()
        except:
            error_detail = e.response.text[:300]

        msg = f"HTTP {status} from {url}\n{error_detail}"
        logger.error(msg)
        raise RuntimeError(msg) from e

    except requests.exceptions.JSONDecodeError:
        logger.error(f"Invalid JSON from {url}")
        raise ValueError(f"Response was not valid JSON: {url}")

    except requests.RequestException as e:
        logger.error(f"Request failed: {url} → {e}")
        raise
