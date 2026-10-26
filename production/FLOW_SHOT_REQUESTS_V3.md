# Hoover Dam v3 — shot tambahan dengan aksi di dalam adegan

Tujuan: gerakan fisik menjadi bagian dari footage, seperti referensi Gateway Arch. Tidak memakai demo Blender atau menyalin footage referensi. Video Flow dibuat manual oleh pengguna; tidak ada panggilan API generasi berbayar.

Paket ini adalah permintaan produksi awal. Pembaruan: keenam klip telah diterima dari pengguna di `assets/supplemental/`. Lima dipilih untuk integrasi; klip penuangan baru disimpan tetapi tidak dipilih karena tampak berupa batu/agregat kering. Lihat `production/supplemental_shots_v3.json` dan `output/revision_v3/final/QA_final.md` untuk status serta pilihan edit terbaru.

## Cara produksi

- Pertahankan `assets/video/scene_01.mp4` sampai `scene_14.mp4` dan voiceover asli. Simpan hasil baru ke `assets/supplemental/` dengan nama di bawah.
- Buat tiap kandidat sebagai satu klip 8 detik vertikal 9:16, tanpa teks, subtitle, logo, watermark, musik atau dialog. Audio tidak diperlukan; edit tetap memakai voiceover asli.
- Jika fitur referensi tersedia, gunakan frame dari aset proyek Anda sendiri untuk menjaga geologi, alat dan material konsisten. Video referensi Gateway Arch menjadi arahan bahasa visual; jangan masukkan footage atau watermark-nya sebagai aset.
- Utamakan satu aksi yang jelas per shot. Kamera bergerak secukupnya agar mekanisme terbaca. Jangan mengandalkan tulisan hasil generasi untuk menyampaikan angka; teks ditambahkan saat editing.
- Rentang edit mengikuti narasi yang sudah ada. Klip baru tidak otomatis menambah durasi film. Periksa hasil sebelum memilih 3–5 detik terbaik; scene 09 memerlukan sekitar 5.43 detik sehingga klip 8 detik memberi ruang pemilihan.
- Hindari objek yang berubah bentuk, sungai yang hilang mendadak, beton yang naik tanpa proses timelapse yang jelas, alat modern, atau pipa yang menembus beton secara tidak masuk akal. Tolak hasil yang gagal, lalu perbaiki prompt manual; jangan menutupi kesalahan dengan angka/anotasi yang menyesatkan.

## Prioritas 1 — air di dalam pipa pendingin

**Tujuan:** scene 11, sekitar 46.50–51.27 detik. Footage sekarang memperlihatkan jaringan pipa, tetapi transport air dan perpindahan panas kurang terbaca.

**Simpan:** `assets/supplemental/scene_11_cooling_action_v3.mp4`

**Prompt Flow (English):**

> A single continuous eight-second vertical 9:16 engineering visualization of a concrete construction block at Hoover Dam in the 1930s. Begin close to a believable embedded steel cooling-pipe bend, then glide slowly sideways to reveal the network inside a clean localized cutaway of the concrete. Cool water is visibly moving inside the opened pipe section while the surrounding concrete and steel remain fixed and physically consistent. Use a restrained natural blue tint only inside the water, no neon trails, arrows, labels, diagrams on a separate background, or glowing walls. Seconds 0–2 establish the real concrete and pipe surface; seconds 2–6 clearly show continuous water movement through the pipe bend; seconds 6–8 hold a readable cutaway view. Cinematic natural light, detailed realistic concrete aggregate and steel, calm camera, no people required, no speech, music, captions, logos or watermarks. The visualization is illustrative, not authentic archival footage. Do not show the whole dam instantly cooling or solidifying.

**Lulus jika:** aliran bergerak di dalam pipa, bentuk pipa tetap, cutaway menyatu dengan material beton. Tidak mengubah warna seluruh beton menjadi indikator suhu palsu.

## Prioritas 2 — pengalihan sungai sebagai aksi sebab-akibat

**Tujuan:** scene 03 atau bagian scene 05, sekitar 9.33–13.57 / 17.60–22.27 detik. Pilih sesuai hasil, jangan gunakan satu shot berulang untuk dua bagian tanpa alasan.

**Simpan:** `assets/supplemental/scene_03_diversion_action_v3.mp4`

**Prompt Flow (English):**

> Eight-second continuous photorealistic vertical 9:16 shot of an illustrative early-1930s Colorado River diversion in rugged Black Canyon at the Hoover Dam construction site. Oblique elevated camera view with natural canyon rock, muddy river current and a clearly visible tunnel entrance in the canyon wall. Water continuously bends toward and enters the real tunnel opening; show convincing current and foam direction, not a painted line or floating arrow. Keep the river, tunnel and cliff geometry stable throughout the shot. Seconds 0–2 establish the river and portal, seconds 2–6 follow the moving current toward the portal with a restrained camera glide, seconds 6–8 hold the flowing entrance. The shot shows one visible portal clearly rather than inventing four identical entrances in a row; the wider four-tunnel context will be explained by narration and other footage. No completed dam, modern bridge, modern equipment, text, labels, split screen, diagram board, voice, music, logo or watermark. This is an illustrative historical reconstruction, not archival footage.

**Lulus jika:** air masuk ke portal, bukan keluar dari portal yang sedang diklaim sebagai inlet. Tidak membuat empat portal identik di satu sisi demi memenuhi angka narasi.

## Prioritas 3 — pertumbuhan blok beton yang bisa diikuti mata

**Tujuan:** scene 10, sekitar 42.07–46.50 detik. Klip sekarang sudah berisi pertumbuhan struktur; kandidat baru hanya dipakai jika prosesnya lebih jelas.

**Simpan:** `assets/supplemental/scene_10_block_growth_v3.mp4`

**Prompt Flow (English):**

> A single eight-second vertical 9:16 historical construction timelapse inside Black Canyon during Hoover Dam construction, 1933–1935. Show adjacent concrete construction blocks and period timber formwork as the main subjects, with a cableway concrete bucket and small distant workers supplying the process. The scene itself visibly progresses: one block receives a lift, neighboring formwork progresses, and the stepped arrangement rises gradually over compressed construction time. Keep the canyon, existing blocks and camera perspective consistent; blocks must not float into position, inflate, melt, or appear fully formed from empty space. Start on a readable close-medium view for two seconds, show the controlled timelapse progression over the next four seconds, then gently reveal adjacent blocks for the last two seconds. Realistic gray concrete, restrained natural light and camera movement, no modern machinery, diagram background, arrows, text, speech, music, logo or watermark. Illustrative historical reconstruction, not archival footage.

**Lulus jika:** kemajuan konstruksi terbaca sebagai timelapse, bukan benda mengembang secara ajaib. Jangan menambah sambungan seperti bata yang tidak sesuai metode konstruksi.

## Cadangan — penuangan beton yang lebih jelas

**Tujuan:** scene 09, sekitar 36.63–42.07 detik. Klip yang ada sudah menampilkan penuangan; ini pilihan pengganti jika diperlukan.

**Simpan:** `assets/supplemental/scene_09_concrete_pour_v3.mp4`

**Prompt Flow (English):**

> One uninterrupted eight-second vertical 9:16 close-medium cinematic shot of a period-appropriate cableway concrete bucket pouring wet concrete into timber block formwork at Hoover Dam in 1933. The bucket gate opens visibly and a heavy, continuous concrete mix falls under gravity, accumulating naturally inside the form. Workers remain at a safe distance with consistent anatomy and period clothing. Establish the bucket for the first two seconds, show the pour clearly for the middle four seconds, then reveal the receiving form while continuing the action for the final two seconds. The bucket stays attached to its cable, material does not turn into sand or disappear, no impossible machinery motion. Keep the pouring action central for a vertical crop. Natural canyon lighting, realistic scale and aggregate texture, no modern excavator or safety gear, text, arrows, music, dialogue, logo or watermark. Illustrative reconstruction, not real archival footage.

**Lulus jika:** material jatuh dari gate bucket dan menumpuk di formwork; ukuran bucket, kabel dan pekerja stabil.

## Cadangan — area kerja mengering tanpa artefak

**Tujuan:** scene 06, sekitar 22.27–27.30 detik. Gunakan klip saat ini jika hasil baru kurang masuk akal.

**Simpan:** `assets/supplemental/scene_06_dry_worksite_v3.mp4`

**Prompt Flow (English):**

> Eight-second continuous elevated vertical 9:16 view of the protected Hoover Dam construction area in early-1930s Black Canyon, shown as a clearly illustrative time-compressed historical reconstruction. Existing temporary earthen cofferdams isolate a central work area while water continues along a separate diversion route. Across the shot the water level within the protected area gradually lowers and wet sediment becomes visible; it must not vanish instantly or turn directly into a fully built concrete dam. Seconds 0–2 establish the barriers and remaining water, seconds 2–6 show the central water surface lowering over compressed time, seconds 6–8 hold the exposed damp worksite. Fixed believable canyon geography, subtle camera movement, no abrupt internal cuts or split screens, no modern machinery, labels, arrows, dialogue, music, logo or watermark.

**Lulus jika:** air tetap punya jalur kontinu di luar area kerja; cofferdam tidak tiba-tiba berubah menjadi bendungan final.

## Cadangan — Black Canyon tanpa inset dan struktur modern

**Tujuan:** scene 02, sekitar 4.77–9.33 detik. Mengatasi inset/struktur yang sudah tertanam pada klip sekarang.

**Simpan:** `assets/supplemental/scene_02_black_canyon_v3.mp4`

**Prompt Flow (English):**

> Single uninterrupted eight-second vertical 9:16 aerial-style historical reconstruction of raw Black Canyon and the free-flowing Colorado River before Hoover Dam construction in 1931. Show rugged Nevada-Arizona desert geology, steep canyon walls and a natural river course. A restrained forward camera glide reveals the depth and scale. No completed dam, intake towers, power station, modern bridge, buildings from the finished project, inset, montage, split screen, text, arrows, people talking, music, logo or watermark. Cinematic realistic natural daylight and stable rock geometry. This is an illustrative pre-construction reconstruction, not authentic archival footage.

**Lulus jika:** satu pandangan kontinu tanpa inset, tidak ada struktur hasil proyek yang sudah selesai.

## Setelah hasil tersedia

Unggah kandidat baru atau simpan pada path yang diusulkan. Editor akan memeriksa durasi, frame awal/tengah/akhir, kontinuitas fisik dan kesesuaian narasi sebelum mengganti pilihan edit pada konfigurasi. Jangan menimpa klip original. Anotasi hanya diaktifkan setelah koordinatnya diperiksa pada footage baru; keyframe lama tidak otomatis cocok.

## Frame referensi visual dari aset sendiri

Folder `production/flow_reference_frames/` berisi enam frame JPG hasil ekstraksi klip asli untuk konsistensi tampilan. Ini bukan footage baru. Jika Flow mendukung image/reference input, pakai frame sesuai scene sebagai referensi material/komposisi, lalu gunakan prompt aksi di atas. Frame scene 02 tetap mengandung keterbatasan visual klip asli; gunakan hanya sebagai referensi geologi, jangan pertahankan struktur proyek yang sudah selesai atau inset.
