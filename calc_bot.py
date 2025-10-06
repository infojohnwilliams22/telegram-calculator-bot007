from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

def number_to_bangla_word(num):
    bangla_numbers = {
        0: "শূন্য", 1: "এক", 2: "দুই", 3: "তিন", 4: "চার", 5: "পাঁচ",
        6: "ছয়", 7: "সাত", 8: "আট", 9: "নয়", 10: "দশ",
        20: "বিশ", 30: "ত্রিশ", 40: "চল্লিশ", 50: "পঞ্চাশ",
        60: "ষাট", 70: "সত্তর", 80: "আশি", 90: "নব্বই", 100: "একশ"
    }
    return bangla_numbers.get(num, str(num))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! আমি আপনার হিসাব বট। যেমন লিখুন: 10+20-5*2")

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        result = eval(text)
        bangla_word = number_to_bangla_word(int(result))
        await update.message.reply_text(f"আপনার মোট হিসাব: {result} ({bangla_word}) ✅")
    except Exception:
        await update.message.reply_text("⚠️ দুঃখিত, হিসাবটা বুঝতে পারিনি। যেমন লিখুন: 10+20-5")

app = ApplicationBuilder().token("8224902232:AAFmDbtTjpU1Ga-A34m9CeQUc3tiT5O4x44").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
app.run_polling()
