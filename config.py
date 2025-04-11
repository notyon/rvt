import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "rvt") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001979450020"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001721745890")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1001775724013"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "1613540894"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#111 #112 #boy #girl #spill #story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Kamu tidak dapat menggunakan bot 🙅, untuk mengirim pesan ke @randomvirtualfess harap join terlebih dahulu ke channel dan grup rvt yang ada dibawah, jika sudah tekan coba lagi atau /help.

Seputar informasi, pertanyaan dan top up coin Rp. 1000 / 200 coin hubungi @xvilance
""")
start_msg = os.getenv("START_MSG", """
Halo {mention}

RVT Menfess bot adalah bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim menfess, gunakan hastag dibawah untuk mengirim pesan:

#boy : untuk mencari teman jika kamu seorang cowo.
#girl : untuk mencari teman jika kamu seorang cewe.
#spill : untuk spill sesuatu.
#story : untuk berbagi cerita/pengalaman.
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#boy : untuk mencari teman jika kamu seorang cowo.
#girl : untuk mencari teman jika kamu seorang cewe.
#spill : untuk spill sesuatu
#story : untuk berbagi cerita/pengalaman.

jangan lupa join @RGCIndo
""")
