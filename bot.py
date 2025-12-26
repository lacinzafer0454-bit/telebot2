import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder

# ENV VARIABLES (REQUIRED)
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise RuntimeError("BOT_TOKEN or CHAT_ID not set in environment variables")

CHAT_ID = int(CHAT_ID)

TEXT = (
    "📷 *Taking Instagram Bans / Unbans Cases*\n\n"
    "*Unban Cases Covered:*\n"
    "• Fraud & Deceptive Activity\n"
    "• Impersonation (Celebrity / Business)\n"
    "• Under 13 Age Restriction\n"
    "• Spam Violations\n"
    "• Review / Appeal Stuck\n\n"
    "💵 *Pricing:* Starting from *$200* (Manual)\n"
    "⏳ *Time Frame:* 1–7 Days (Max)\n"
    "⭐ *High Success Rate*\n\n"
    "_______\n\n"
    "📱 *INSTAGRAM / TIKTOK / FACEBOOK REMOVAL SERVICE*\n\n"
    "• Human PFP Accounts\n"
    "• Business Accounts\n"
    "• Most Account Types Supported\n\n"
    "⚡ Fast Results | High Success\n"
    "💰 Price Starting: *XX$*\n\n"
    "🤝 *Any Reputed Middleman Accepted*"
)

keyboard = [
    [InlineKeyboardButton("Contact", url="https://t.me/shajwals")],
    [InlineKeyboardButton("We Offer", url="https://t.me/shajwaloffers")],
    [InlineKeyboardButton("PW’S", url="https://t.me/shajwalbans")]
]

reply_markup = InlineKeyboardMarkup(keyboard)


async def send_notifications(bot):
    while True:
        try:
            await bot.send_message(
                chat_id=CHAT_ID,
                text=TEXT,
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            print("Message sent")
        except Exception as e:
            print("Error:", e)

        await asyncio.sleep(60)  # 1 minute


async def main():
    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .job_queue(None)  # disable APScheduler
        .build()
    )

    asyncio.create_task(send_notifications(app.bot))

    await app.initialize()
    await app.start()
    await asyncio.Event().wait()  # keep alive forever


if __name__ == "__main__":
    asyncio.run(main())
