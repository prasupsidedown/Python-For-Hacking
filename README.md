<div align="center">
    <h1>Python Networking with TCP & UDP</h1>
    <h3>Dasar-dasar Komunikasi Jaringan Menggunakan Python</h3>
    <p>Dokumentasi ini menjelaskan implementasi protokol TCP dan UDP menggunakan bahasa Python, serta memberikan contoh
    program server dan client yang dapat dijalankan secara langsung.</p>
</div>

<hr/>

<h2 id="deskripsi">1. Deskripsi Proyek</h2>
<p>
    Proyek ini berisi contoh penerapan socket programming menggunakan Python. Tujuan utama dari repository ini adalah
    memberikan gambaran jelas tentang bagaimana proses komunikasi jaringan berlangsung pada dua protokol utama: 
    <b>TCP (Transmission Control Protocol)</b> dan <b>UDP (User Datagram Protocol)</b>.
</p>

<ul>
    <li>Memahami alur komunikasi client–server</li>
    <li>Membedakan perilaku TCP dan UDP</li>
    <li>Mengirim dan menerima data menggunakan socket Python</li>
    <li>Menguji aplikasi jaringan secara lokal</li>
</ul>

<hr/>

<h2 id="fitur">2. Fitur</h2>

<h3>TCP</h3>
<ul>
    <li>Bersifat connection-oriented</li>
    <li>Menjamin data diterima secara utuh dan berurutan</li>
    <li>Terdapat proses accept, recv, dan send yang terstruktur</li>
</ul>

<h3>UDP</h3>
<ul>
    <li>Tidak membutuhkan koneksi</li>
    <li>Pengiriman sangat cepat</li>
    <li>Cocok untuk aplikasi real-time</li>
</ul>

<hr/>

<h2 id="protokol">3. Penjelasan Protokol</h2>

<h3>3.1 TCP Server</h3>
<p>Proses umum yang dilakukan server:</p>
<pre>
1. Membuat socket bertipe SOCK_STREAM
2. Binding ke alamat dan port tertentu
3. Mendengarkan koneksi masuk
4. Menerima client
5. Menerima pesan dan memprosesnya
6. Mengirimkan balasan
7. Menutup koneksi
</pre>

<h3>3.2 TCP Client</h3>
<pre>
1. Membuat socket TCP
2. Menghubungkan ke server
3. Mengirim pesan
4. Menerima balasan
5. Menampilkan hasil
6. Menutup koneksi
</pre>

<h3>3.3 UDP Server</h3>
<pre>
1. Membuat socket SOCK_DGRAM
2. Binding port
3. Menunggu datagram masuk
4. Menampilkan pesan yang diterima
5. Mengirimkan respon
</pre>

<h3>3.4 UDP Client</h3>
<pre>
1. Membuat socket UDP
2. Mengirimkan datagram
3. Menunggu balasan
4. Menampilkan hasil
</pre>

<hr/>

<h2 id="perbandingan">4. Perbandingan TCP dan UDP</h2>

<table border="1" cellspacing="0" cellpadding="8">
    <tr>
        <th>Aspek</th>
        <th>TCP</th>
        <th>UDP</th>
    </tr>
    <tr>
        <td>Jenis Protokol</td>
        <td>Connection-oriented</td>
        <td>Connectionless</td>
    </tr>
    <tr>
        <td>Kecepatan</td>
        <td>Lebih lambat</td>
        <td>Sangat cepat</td>
    </tr>
    <tr>
        <td>Keandalan</td>
        <td>Menjamin data sampai</td>
        <td>Tidak dijamin</td>
    </tr>
    <tr>
        <td>Urutan Data</td>
        <td>Dijaga</td>
        <td>Tidak dijaga</td>
    </tr>
    <tr>
        <td>Penggunaan Ideal</td>
        <td>Web, pengiriman file, protokol aman</td>
        <td>VoIP, streaming, game online</td>
    </tr>
</table>

<hr/>

<h2 id="cara-menjalankan">5. Cara Menjalankan Program</h2>

<h3>Menjalankan TCP Server</h3>
<pre>
python tcpServer.py
</pre>

<h3>Menjalankan TCP Client</h3>
<pre>
python tcpSocket.py
</pre>

<h3>Menjalankan UDP Server</h3>
<pre>
python udpServer.py
</pre>

<h3>Menjalankan UDP Client</h3>
<pre>
python udpSocket.py
</pre>

<hr/>

<h2 id="struktur">6. Struktur Direktori</h2>

<pre>
project/
│
├── tcp/
│   ├── tcpServer.py
│   └── tcpSocket.py
│
├── udp/
│   ├── udpServer.py
│   └── udpSocket.py
│
└── README.md
</pre>

<hr/>

<h2 id="troubleshoot">7. Troubleshooting</h2>

<h3>Port sudah digunakan</h3>
<pre>
netstat -ano | findstr :12345
netstat -ano | findstr :9997
</pre>

<h3>Connection refused</h3>
<ul>
    <li>Pastikan server dijalankan lebih dulu</li>
    <li>Periksa IP dan port</li>
    <li>Nonaktifkan firewall untuk pengujian lokal</li>
</ul>

<h3>Error module</h3>
<p>Socket adalah modul bawaan Python, sehingga tidak memerlukan instalasi tambahan.</p>

<hr/>

<div align="center">
</div>
