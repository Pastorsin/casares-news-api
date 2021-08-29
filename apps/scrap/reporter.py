import logging
from datetime import datetime

from django.conf import settings
from telegram import Bot, ParseMode

logger = logging.getLogger(__name__)

TOKEN = settings.TELEGRAM_TOKEN
CHAT_ID = settings.TELEGRAM_CHAT_ID


def report(results):
    message = generate_message(results)
    logger.info(message)

    if TOKEN:
        send_telegram_message(message)


def generate_message(results):
    lines = []
    total_scraped = total_created = total_time = 0

    lines.append(header())

    for result in results:
        stats = result["stats"]

        lines.append(entry(**stats, heading=result["scraper"]))

        total_scraped += stats["scraped"]
        total_created += stats["created"]
        total_time += stats["time"]

    lines.append(separator(lines))
    lines.append(
        entry(total_scraped, total_created, total_time, heading="TOTAL")
    )

    return _build_message(lines)


def header():
    return f"Execution at {datetime.now().isoformat()}"


def entry(scraped, created, time, heading):
    return f"{heading:<25} scraped={scraped} created={created} time={time:.2f}s"


def separator(lines):
    width = max(map(len, lines))
    return "-" * width


def _build_message(lines):
    text = "\n".join(lines)
    markdown_block = f"```\n{text}\n```"
    return markdown_block


def send_telegram_message(message):
    bot = Bot(token=TOKEN)
    bot.send_message(
        chat_id=CHAT_ID, parse_mode=ParseMode.MARKDOWN, text=message
    )
