import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "6943283709:AAH1UYtRMaDhvUFnrjnNc0J6g0paS2haR4o")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "fwbx1") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001197188587"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001689707975")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002109996381"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "3"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#111 #112 #FwbBoy #FwbGirl #FwbSpill #FwbStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Kamu tidak dapat menggunakan bot 🙅, untuk mengirim pesan ke @friendwithbenefitx harap join terlebih dahulu ke channel dan grup cpf yang ada dibawah, jika sudah tekan coba lagi atau /help.

Seputar informasi, pertanyaan dan top up coin bisa langsung hubungi @CPFServiceBOT
""")
start_msg = os.getenv("START_MSG", """
Halo {mention}

fwbbase bot adalah bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim menfess, gunakan hastag dibawah untuk mengirim pesan:

#FwbBoy : untuk mencari teman jika kamu seorang cowo.
#FwbGirl : untuk mencari teman jika kamu seorang cewe.
#FwbSpill : untuk spill sesuatu.
#FwbStory : untuk berbagi cerita/pengalaman.
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#FwbBoy : untuk mencari teman jika kamu seorang cowo.
#FwbGirl : untuk mencari teman jika kamu seorang cewe.
#FwbSpill : untuk spill sesuatu
#FwbStory : untuk berbagi cerita/pengalaman.

jangan lupa join @caripartnerfwb
""")
