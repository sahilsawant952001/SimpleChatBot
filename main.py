import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('API_KEY'))

@bot.message_handler(commands=['Hi'])
def hi(message):
    bot.send_message(message.chat.id, 'Welcome To KYC Verification System use below commands for further information '
                                      '\n /About \n /Website \n /Steps \n')


@bot.message_handler(commands=['About'])
def about(message):
    bot.send_message(message.chat.id, 'The know your customer or know your client (KYC) guidelines in financial services require that professionals make an effort to verify the identity, suitability, and risks involved with maintaining a business relationship. The procedures fit within the broader scope of a bank AntiMoney Laundering (AML) policy. KYC processes are also employed by companies of all sizes for the purpose of ensuring their proposed customers, agents, consultants, or distributors are anti-bribery compliant, and are actually who they claim to be. Banks, insurers, export creditors, and other financial institutions are increasingly demanding that customers provide detailed due diligence information. Initially, these regulations were imposed only on the financial institutions but now the non-financial industry, fintech, virtual assets dealers, and even non-profit organizations are liable to oblige.')


@bot.message_handler(commands=['Website'])
def website(message):
    bot.send_message(message.chat.id, 'Visit Our Website : www.kyc.com')


@bot.message_handler(commands=['Steps'])
def steps(message):
    bot.send_message(message.chat.id, '1) Collection of Information : The first step in KYC verification involves the collection of personal information from an online user. The user is supposed to enter all the personal details at the time of account registration. \n2) Upload an Evidence : After collecting information, in the second step, ask the user to upload a supporting piece of evidence as an identity proof. This helps the system verify that the user-entered information is not fake and holds authentic data. \n3) Verification of information : Once the user uploads a document as proof, the document template is identified and examined against several checks. It is to ensure the uploaded document is not tampered or photoshopped. Once it’s validated, the data is extracted. There can be two ways to fetch the data from documents \n')


bot.polling()
