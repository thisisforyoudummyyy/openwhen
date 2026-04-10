import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ✏️ EDIT YOUR MESSAGES HERE
WELCOME_MESSAGE = "Hi love 💛 I made this for you. How are you feeling right now?"

MESSAGES = {
    "happy":   "I'm so glad you're happy today 😊 You deserve every bit of it. Keep shining!",
    "sad":     "Hey, it's okay to feel sad 💙 I'm always here for you, even when I'm not around.",
    "bored":   "Bored huh? 😄 Go drink some water, take a walk, and remember I'm thinking of you!",
    "stressed":"Take a deep breath 🌿 You've handled hard things before and you'll get through this too.",
    "tired":   "Rest, you've earned it 🌙 Don't feel guilty for taking care of yourself.",
    "loved":   "Good 🥹 Because you are so so loved. Never forget that. 💛",
}

# ✏️ EDIT BUTTON LABELS HERE (emoji + name)
BUTTON_LABELS = {
    "happy":    "😊 Happy",
    "sad":      "😢 Sad",
    "bored":    "😴 Bored",
    "stressed": "😰 Stressed",
    "tired":    "😪 Tired",
    "loved":    "🥰 Loved",
}

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    row = []
    for key, label in BUTTON_LABELS.items():
        row.append(InlineKeyboardButton(label, callback_data=key))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_tap(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mood = query.data
    msg = MESSAGES.get(mood, "No message found for this mood.")
    await query.message.reply_text(msg)

app = ApplicationBuilder().token("8798005985:AAGJh-7_aWPKufiySBocnZJ5sYrcrysMCxc").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_tap))

print("Bot is running...")
app.run_polling()