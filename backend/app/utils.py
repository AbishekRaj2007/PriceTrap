import statistics

def detect_fake_discount(prices, current_price):
    if len(prices) < 3:
        return {
            "status": "INSUFFICIENT_DATA",
            "confidence": 0.0
        }

    median_price = statistics.median(prices)

    ratio = current_price / median_price

    if ratio >= 0.9:
        return {
            "status": "FAKE",
            "confidence": round(1 - ratio, 2)
        }

    elif 0.7 <= ratio < 0.9:
        return {
            "status": "SUSPICIOUS",
            "confidence": round(1 - ratio, 2)
        }

    else:
        return {
            "status": "GENUINE",
            "confidence": round(1 - ratio, 2)
        }
