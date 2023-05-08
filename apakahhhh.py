# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Menu Utama",
        ("Home", "Perkenalan Kelompok", "Perhitungan Normalitas", "PerHitungan Kadar (%b/v)", "Perhitungan kadar (%b/b)")
    )
	
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Normalitas dan Kadar")
   st.writer('Normalitas adalah ukuran yang menunjukkan konsentrasi dengan berat setara dalam gram per liter larutan, dimana berat setara itu sendiri adalah ukuran kapasitas reaktif dari suatu molekul yang terlarut dalam larutan. Dalam reaksi, peran zat terlarut tersebut adalah akan menentukan normalitas suatu larutan.')
   st.writer('Persentase berat per volume (% b/v) Persentase b/v adalah jumlah gram zat terlarut dalam tiap 100 ml larutan. %b/v= x100% Satuan %b/v umumnya dipakai untuk zat terlarut padat dalam pelarut cair.')
   st.writer('Persen b/b adalah jumlah gram zat terlarut dalam tiap 100 gram larutan. %b/b = x100% Contoh: Larutan cuka sebanyak 40 gram mengandung asam asetat sebanyak 2 gram.')

with col2:
   st.header("Perkenalan Kelompok")
   st.text('Berkembangnya teknologi informasi memudahkan manusia untuk mengakses informasi kapanpun dan dimanapun. Sekarang banyak bermunculan website-website yang menyediakan berbagai macam kebutuhan yang sangat membantu dalam kehidupan terutama bagi para pelajar. Salah satu perkembangan teknologi informasi dimanfaatkan dalam bidang Pendidikan. Kita bisa membuat sesuatu yang bisa membantu dalam belajar. Contohnya membantu mempercapat proses menghitung yang dimana orang- orang biasanya mengalami kesulitan. Dalam dunia kimia, perhitungan merupakan salah satu aspek penting dalam menentukan hasil akhir dari suatu percobaan atau penelitian. Oleh karena itu, keakuratan perhitungan sangat diperlukan untuk mendapatkan hasil yang valid dan dapat dipercaya. Namun, perhitungan kimia yang kompleks membutuhkan pemahaman matematika yang tinggi dan rumit, sehingga dapat menghambat produktivitas dan efisiensi dalam melakukan penelitian. Dengan adanya website perhitungan kimia, pengguna dapat dengan mudah mengakses perhitungan yang akurat dan cepat tanpa harus memikirkan rumus dan langkah-langkah yang rumit. Oleh karena itu, kami membuat website perhitungan normalitas dan kadar. Website ini bisa membantu melakukan perhitungan kimia secara efektif dan efisien. Wesite ini juga dapat diakses oleh siapa saja dan kapan saja, sehingga memudahkan pengguna yang berada di berbagai tempat dan memiliki waktu yang terbatas. Website ini dapat meningkatkan kualitas dan efektivitas dalam melakukan penelitian dan percobaan kimia. Hal ini karena pengguna dapat lebih fokus pada hasil akhir daripada melakukan perhitungan secara manual. Oleh karena itu, pembuatan website perhitungan kimia sangat penting dalam mendukung kemajuan dan pengembangan ilmu kimia.')
	
