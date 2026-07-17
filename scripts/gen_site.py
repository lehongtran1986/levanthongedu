#!/usr/bin/env python3
"""Generates all HTML pages for the LêVănThông Education website from data in this file.

Run from anywhere: python3 scripts/gen_site.py
Regenerates every .html file at repo root and under programs/ — never
hand-edit the generated .html files directly, edit this script instead.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CENTER_NAME = "Lê Văn Thông Education"
TAGLINE = "Luyện thi đại học đánh giá năng lực (Toán – Vật lý – Tiếng Anh), đồng thời xây nền tảng vững chắc từ lớp 6 - 12 tại Quận Bình Thạnh"
PHONE_DISPLAY = "0919 222 595"
PHONE_TEL = "tel:0919222595"
ZALO_LINK = "https://zalo.me/0919222595"
ADDRESS = "232/5 Bình Lợi, Phường Bình Lợi Trung, TP.HCM"
FORM_ENDPOINT = "https://script.google.com/macros/s/AKfycbx1i4SOqN-4OToiwDra2rS-LL9oSJOc3bPgwassONVTdQibTDSWfyY-YrKH993xJiYC_Q/exec"
GA4_MEASUREMENT_ID = "G-V2TYFJNREK"
GA4_CODE = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_MEASUREMENT_ID}');
</script>"""
CLOUDFLARE_ANALYTICS_TOKEN = "83983b7d6b6b4ba7a9c160330a84e206"
CLOUDFLARE_ANALYTICS_CODE = f"""<!-- Cloudflare Web Analytics -->
<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "{CLOUDFLARE_ANALYTICS_TOKEN}"}}'></script>
<!-- End Cloudflare Web Analytics -->"""
FACEBOOK_PIXEL_ID = "1699836964558657"
FACEBOOK_PIXEL_CODE = f"""<!-- Facebook Pixel Code -->
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{FACEBOOK_PIXEL_ID}');
fbq('track', 'PageView');</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id={FACEBOOK_PIXEL_ID}&ev=PageView&noscript=1"/></noscript>
<!-- End Facebook Pixel Code -->"""
MAP_LAT = "10.8348866"
MAP_LNG = "106.7046957"
MAP_EMBED_SRC = f"https://www.google.com/maps?q={MAP_LAT},{MAP_LNG}&z=16&output=embed"
MAP_IFRAME = f'<iframe src="{MAP_EMBED_SRC}" class="w-full h-full rounded-xl border-0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Bản đồ {CENTER_NAME}"></iframe>'

GRADES = [6, 7, 8, 9, 10, 11, 12]
CLASS_SIZE = 6
TUITION = "1.500.000đ/tháng (1 buổi/tuần). Học 2-3 buổi/tuần: mức giá thương lượng, liên hệ trung tâm để được tư vấn"
SCHEDULE_TEXT = "1-3 buổi/tuần tùy theo nhu cầu của học sinh, khai giảng đầu mỗi tháng"

def nav_link(href, label, current):
    active = " text-[--color-accent] font-semibold" if current == href else " text-white"
    return f'<a href="{href}" class="block px-4 py-2 hover:text-[--color-accent] transition{active}">{label}</a>'

NAV_ITEMS = [
    ("/index.html", "Trang chủ"),
    ("/programs/toan.html", "Toán"),
    ("/programs/vatly.html", "Vật lý"),
    ("/programs/anhvan.html", "Anh văn"),
    ("/programs/ielts.html", "IELTS"),
    ("/results.html", "Gương sáng"),
    ("/about.html", "Thầy Lê Văn Thông"),
    ("/contact.html", "Liên hệ"),
]

def header(current):
    desktop_links = "\n      ".join(
        f'<a href="{href}" class="hover:text-[--color-accent] transition{" text-[--color-accent] font-semibold" if href==current else ""}">{label}</a>'
        for href, label in NAV_ITEMS
    )
    mobile_links = "\n        ".join(nav_link(href, label, current) for href, label in NAV_ITEMS)
    return f"""  <header class="sticky top-0 z-50 bg-[--color-primary] text-white shadow-md">
    <div class="max-w-6xl mx-auto flex items-center justify-between px-4 py-3">
      <a href="/index.html" class="flex items-center gap-2 font-bold text-lg">
        <span class="bg-[--color-accent] text-[--color-primary] rounded-full w-9 h-9 flex items-center justify-center">L</span>
        <span class="hidden sm:inline">{CENTER_NAME}</span>
        <span class="sm:hidden">{CENTER_NAME}</span>
      </a>
      <nav class="hidden md:flex items-center gap-6 text-sm">
        {desktop_links}
      </nav>
      <div class="flex items-center gap-2">
        <a href="{PHONE_TEL}" class="hidden sm:flex items-center gap-1 bg-[--color-accent] text-[--color-primary] font-semibold px-3 py-2 rounded-full text-sm">📞 Gọi ngay</a>
        <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="hidden sm:flex items-center gap-1 bg-white text-[--color-primary] font-semibold px-3 py-2 rounded-full text-sm">Zalo</a>
        <button id="menu-toggle" class="md:hidden text-2xl leading-none" aria-label="Mở menu">&#9776;</button>
      </div>
    </div>
    <nav id="mobile-menu" class="hidden md:hidden bg-[--color-primary] border-t border-white/10 pb-3">
        {mobile_links}
        <div class="flex gap-2 px-4 pt-2">
          <a href="{PHONE_TEL}" class="flex-1 text-center bg-[--color-accent] text-[--color-primary] font-semibold px-3 py-2 rounded-full text-sm">📞 Gọi ngay</a>
          <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="flex-1 text-center bg-white text-[--color-primary] font-semibold px-3 py-2 rounded-full text-sm">Zalo</a>
        </div>
    </nav>
  </header>
"""

def footer():
    return f"""  <footer class="bg-[--color-primary] text-white/90 mt-16">
    <div class="max-w-6xl mx-auto px-4 py-10 grid gap-8 sm:grid-cols-2 md:grid-cols-4 text-sm">
      <div>
        <h3 class="font-bold text-white mb-2">{CENTER_NAME}</h3>
        <p>{TAGLINE}</p>
      </div>
      <div>
        <h4 class="font-semibold text-white mb-2">Liên kết</h4>
        <ul class="space-y-1">
          <li><a href="/about.html" class="hover:text-[--color-accent]">Thầy Lê Văn Thông</a></li>
          <li><a href="/method.html" class="hover:text-[--color-accent]">Phương pháp học</a></li>
          <li><a href="/results.html" class="hover:text-[--color-accent]">Gương sáng</a></li>
          <li><a href="/public-info.html" class="hover:text-[--color-accent]">Thông tin công khai</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-semibold text-white mb-2">Khóa học</h4>
        <ul class="space-y-1">
          <li><a href="/programs/toan.html" class="hover:text-[--color-accent]">Toán (Lớp 6–12)</a></li>
          <li><a href="/programs/vatly.html" class="hover:text-[--color-accent]">Vật lý (Lớp 6–12)</a></li>
          <li><a href="/programs/anhvan.html" class="hover:text-[--color-accent]">Anh văn (Lớp 6–12)</a></li>
          <li><a href="/programs/ielts.html" class="hover:text-[--color-accent]">IELTS (Band 5.0–6.5)</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-semibold text-white mb-2">Liên hệ</h4>
        <p>{ADDRESS}</p>
        <p>Điện thoại: <a href="{PHONE_TEL}" class="hover:text-[--color-accent]">{PHONE_DISPLAY}</a></p>
        <p><a href="{ZALO_LINK}" target="_blank" rel="noopener" class="hover:text-[--color-accent]">Nhắn Zalo</a></p>
      </div>
    </div>
    <div class="border-t border-white/10 text-center text-xs py-4">&copy; 2026 {CENTER_NAME}. All rights reserved.</div>
  </footer>

  <div class="sticky-actions sm:hidden flex">
    <a href="{PHONE_TEL}" class="flex-1 text-center bg-[--color-accent] text-[--color-primary] font-bold py-3">📞 Gọi ngay</a>
    <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="flex-1 text-center bg-[--color-primary] text-white font-bold py-3 border-l border-white/20">Nhắn Zalo</a>
  </div>
"""

def page(title, description, current, body, asset_prefix="", extra_head=""):
    css_path = f"{asset_prefix}css/styles.css"
    js_path = f"{asset_prefix}js/main.js"
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="geo.position" content="10.8031, 106.7292">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="{css_path}">
  {extra_head}
  {GA4_CODE}
  {FACEBOOK_PIXEL_CODE}
  {CLOUDFLARE_ANALYTICS_CODE}
</head>
<body class="bg-white text-gray-800 pb-16 sm:pb-0">
{header(current)}
{body}
{footer()}
  <script src="{js_path}"></script>
</body>
</html>
"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

# ---------- index.html ----------
index_body = f"""  <main>
    <section class="bg-gradient-to-b from-[--color-primary] to-[#002a57] text-white">
      <div class="max-w-6xl mx-auto px-4 py-14 sm:py-20 text-center">
        <h1 class="text-3xl sm:text-5xl font-bold leading-tight">Vững vàng luyện thi đại học và đánh giá năng lực<br class="hidden sm:block"> cùng nền tảng Toán – Lý – Anh và IELTS từ lớp 6 - 12</h1>
        <p class="mt-2 text-[--color-accent] font-semibold">Học cùng đội ngũ giảng dạy dẫn dắt bởi Thầy Lê Văn Thông</p>
        <div class="mt-8 flex flex-col sm:flex-row gap-3 justify-center">
          <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="bg-[--color-accent] text-[--color-primary] font-bold px-6 py-3 rounded-full">Tư vấn qua Zalo</a>
          <a href="/method.html" class="bg-white/10 border border-white/40 text-white font-semibold px-6 py-3 rounded-full">Nhận lộ trình cá nhân hóa</a>
        </div>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 py-10">
      <h2 class="text-2xl font-bold text-center text-[--color-primary]">Vì sao chọn trung tâm</h2>
      <div class="mt-6 grid sm:grid-cols-2 md:grid-cols-5 gap-4">
        <div class="p-4 border rounded-xl text-center"><div class="text-3xl mb-2">🎯</div><p class="text-sm font-medium">Lộ trình cá nhân hóa theo năng lực</p></div>
        <div class="p-4 border rounded-xl text-center"><div class="text-3xl mb-2">👨‍🏫</div><p class="text-sm font-medium">Thầy Lê Văn Thông cùng đội ngũ giảng dạy giàu kinh nghiệm</p></div>
        <div class="p-4 border rounded-xl text-center"><div class="text-3xl mb-2">📊</div><p class="text-sm font-medium">Theo dõi tiến độ hiệu quả</p></div>
        <div class="p-4 border rounded-xl text-center"><div class="text-3xl mb-2">🏫</div><p class="text-sm font-medium">Lớp học sĩ số ít</p></div>
        <div class="p-4 border rounded-xl text-center"><div class="text-3xl mb-2">📍</div><p class="text-sm font-medium">Vị trí thuận tiện Quận Bình Thạnh</p></div>
      </div>
    </section>

    <section class="bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 py-10 grid sm:grid-cols-2 gap-8 items-center">
        <img src="/assets/images/teacher-whiteboard.jpg" alt="Thầy Lê Văn Thông giảng bài" class="rounded-xl w-full h-auto object-cover aspect-video">
        <div>
          <h2 class="text-2xl font-bold text-[--color-primary]">Gặp Thầy Lê Văn Thông</h2>
          <p class="mt-3 text-gray-600">Nhiều năm kinh nghiệm giảng dạy Toán, Vật lý và Anh văn cho học sinh THCS-THPT, được nhiều phụ huynh học sinh Bình Thạnh tin tưởng.</p>
          <img src="/assets/images/thay-thong-lop-vatly-02.jpg" alt="Thầy Lê Văn Thông trong một buổi giảng dạy" class="rounded-xl mt-4 w-full h-auto object-cover aspect-video">
          <a href="/about.html" class="inline-block mt-4 text-[--color-primary] font-semibold underline">Xem thêm về Thầy &rarr;</a>
        </div>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 py-10">
      <h2 class="text-2xl font-bold text-center text-[--color-primary]">Khóa học nổi bật</h2>
      <div class="mt-6 grid sm:grid-cols-2 md:grid-cols-4 gap-6">
        <div class="border rounded-xl p-5">
          <h3 class="font-bold text-lg">Toán (Lớp 6–12)</h3>
          <p class="text-sm text-gray-600 mt-2">Củng cố nền tảng và nâng cao tư duy Toán học qua từng khối lớp.</p>
          <a href="/programs/toan.html" class="inline-block mt-3 text-[--color-primary] font-semibold underline">Xem chi tiết &rarr;</a>
        </div>
        <div class="border rounded-xl p-5">
          <h3 class="font-bold text-lg">Vật lý (Lớp 6–12)</h3>
          <p class="text-sm text-gray-600 mt-2">Thầy Lê Văn Thông cùng đội ngũ giảng dạy giàu kinh nghiệm, rèn tư duy giải bài tập Vật lý.</p>
          <a href="/programs/vatly.html" class="inline-block mt-3 text-[--color-primary] font-semibold underline">Xem chi tiết &rarr;</a>
        </div>
        <div class="border rounded-xl p-5">
          <h3 class="font-bold text-lg">Anh văn (Lớp 6–12)</h3>
          <p class="text-sm text-gray-600 mt-2">Phát triển ngữ pháp, từ vựng và kỹ năng làm bài thi Anh văn.</p>
          <a href="/programs/anhvan.html" class="inline-block mt-3 text-[--color-primary] font-semibold underline">Xem chi tiết &rarr;</a>
        </div>
        <div class="border rounded-xl p-5">
          <h3 class="font-bold text-lg">IELTS (Band 5.0–6.5)</h3>
          <p class="text-sm text-gray-600 mt-2">Do Thầy Lê Hồng Trân phụ trách, giảng viên UEH với phương pháp giảng dạy tiên tiến.</p>
          <a href="/programs/ielts.html" class="inline-block mt-3 text-[--color-primary] font-semibold underline">Xem chi tiết &rarr;</a>
        </div>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 py-10">
      <h2 class="text-2xl font-bold text-center text-[--color-primary]">Gương sáng</h2>
      <div class="mt-6 border rounded-xl overflow-hidden sm:grid sm:grid-cols-2">
        <img src="/assets/images/guong-sang-phan-hai-anh.jpg" alt="Thầy Lê Văn Thông cùng học sinh Phan Hải Anh" class="w-full h-full object-cover">
        <div class="p-6">
          <h3 class="text-lg font-bold text-[--color-primary]">Phan Hải Anh</h3>
          <p class="mt-3 text-gray-600 text-sm">Chúc mừng em Phan Hải Anh đã xuất sắc được tuyển thẳng vào cả hai trường đại học năm 2026: Học viện Ngoại giao và Trường Đại học Khoa học Xã hội và Nhân văn. Mới ngày nào em còn là cậu học trò nhỏ, bỡ ngỡ bước vào lớp dạy kèm của thầy từ năm lớp 9&hellip;</p>
          <a href="/results.html" class="inline-block mt-4 text-[--color-primary] font-semibold underline">Xem chi tiết &rarr;</a>
        </div>
      </div>
    </section>

    <section class="bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 py-10">
        <h2 class="text-2xl font-bold text-center text-[--color-primary]">Chia sẻ của học sinh và phụ huynh</h2>
        <div class="mt-6 grid sm:grid-cols-3 gap-6">
          <div class="bg-white border rounded-xl p-5 text-sm text-gray-600">"Thầy không chỉ dạy kiến thức mà thực sự đồng hành cùng con trong suốt chặng đường ôn thi, luôn sát sao và động viên kịp thời để con giữ vững mục tiêu vào đại học."<p class="mt-2 font-semibold text-gray-800">— Phụ huynh học sinh</p></div>
          <div class="bg-white border rounded-xl p-5 text-sm text-gray-600">"Lớp học ít bạn nên em được Thầy kèm sát từng buổi, chỗ nào chưa hiểu là hỏi được ngay. Nhờ vậy em tự tin hơn hẳn khi bước vào kỳ thi đại học."<p class="mt-2 font-semibold text-gray-800">— Học sinh lớp 12</p></div>
          <div class="bg-white border rounded-xl p-5 text-sm text-gray-600">"Điều tôi quý nhất ở Thầy là sự kiên trì đồng hành cùng con suốt nhiều năm, từ những buổi học đầu tiên đến khi con vững vàng vươn tới mục tiêu đại học."<p class="mt-2 font-semibold text-gray-800">— Phụ huynh học sinh</p></div>
        </div>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 py-10 grid sm:grid-cols-2 gap-8">
      <div class="aspect-video rounded-xl overflow-hidden">{MAP_IFRAME}</div>
      <div>
        <h2 class="text-2xl font-bold text-[--color-primary]">Thông tin liên hệ</h2>
        <p class="mt-3 text-gray-600">Địa chỉ: {ADDRESS}</p>
        <p class="text-gray-600">Điện thoại: <a href="{PHONE_TEL}" class="text-[--color-primary] font-semibold">{PHONE_DISPLAY}</a></p>
        <p class="text-gray-600">Giờ hoạt động: 8:00 – 21:00, Thứ 2 – Chủ nhật</p>
      </div>
    </section>

    <section id="assessment-form" class="bg-[--color-primary] text-white">
      <div class="max-w-2xl mx-auto px-4 py-12">
        <h2 class="text-2xl font-bold text-center">Tư vấn miễn phí</h2>
        <p class="text-center text-white/80 mt-2">Không cần làm bài kiểm tra đầu vào — nhắn Zalo, đội ngũ trung tâm sẽ tư vấn ngay.</p>
        <div class="mt-6 text-center">
          <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="inline-block bg-[--color-accent] text-[--color-primary] font-bold px-8 py-4 rounded-full text-lg shadow-lg hover:scale-105 transition-transform">Tư vấn qua Zalo</a>
        </div>
      </div>
    </section>
  </main>
"""
write("index.html", page(
    "Trang chủ | " + CENTER_NAME,
    "LêVănThông Education dạy Toán, Vật lý, Tiếng Anh cho học sinh lớp 6-12 tại Quận Bình Thạnh, tập trung luyện thi đại học đánh giá năng lực. Lớp học nhỏ, lịch học linh hoạt, theo dõi tiến độ hàng tuần.",
    "/index.html", index_body))

# ---------- subject program page (Toán / Vật lý / Anh văn, lớp 6-12) ----------
GRADE_LEVELS = [f"Lớp {g}" for g in GRADES]
IELTS_LEVELS = ["Band 5.0", "Band 5.5", "Band 6.0", "Band 6.5"]

SUBJECTS = {
    "toan": {
        "name": "Toán",
        "title_suffix": "(Lớp 6–12)",
        "summary": "Chương trình Toán từ lớp 6 đến lớp 12, củng cố nền tảng và luyện thi theo từng giai đoạn.",
        "levels": GRADE_LEVELS,
        "level_col_header": "Khối lớp",
        "focus": {
            "Lớp 6": "Số học, hình học cơ bản, làm quen tư duy logic",
            "Lớp 7": "Đại số, hình học lớp 7, tỉ lệ thức",
            "Lớp 8": "Phương trình, bất phương trình, hình học không gian cơ bản",
            "Lớp 9": "Ôn thi vào lớp 10: hệ phương trình, hàm số, hình học phẳng",
            "Lớp 10": "Hàm số, phương trình, lượng giác cơ bản",
            "Lớp 11": "Tổ hợp – xác suất, dãy số, lượng giác nâng cao",
            "Lớp 12": "Ôn thi THPT: khảo sát hàm số, tích phân, hình học không gian",
        },
        "audience": "Học sinh lớp 6 đến lớp 12",
        "instructor": "Thầy Lê Văn Thông và đội ngũ giảng dạy",
        "eligibility_q": "Học sinh lớp nào có thể đăng ký?",
        "eligibility_a": "Trung tâm nhận học sinh từ lớp 6 đến lớp 12, xếp lớp theo năng lực thực tế.",
        "teacher_bio": "",
        "subject_image": "",
    },
    "vatly": {
        "name": "Vật lý",
        "title_suffix": "(Lớp 6–12)",
        "summary": "Chương trình Vật lý từ lớp 6 đến lớp 12, trực tiếp Thầy Lê Văn Thông giảng dạy.",
        "levels": GRADE_LEVELS,
        "level_col_header": "Khối lớp",
        "focus": {
            "Lớp 6": "Làm quen phương pháp học Vật lý, đo lường cơ bản",
            "Lớp 7": "Âm học, quang học cơ bản",
            "Lớp 8": "Cơ học, áp suất, nhiệt học cơ bản",
            "Lớp 9": "Điện học, điện từ học",
            "Lớp 10": "Cơ học: động học, động lực học",
            "Lớp 11": "Điện học, điện từ trường, dòng điện",
            "Lớp 12": "Ôn thi THPT: dao động, sóng, điện xoay chiều, hạt nhân",
        },
        "audience": "Học sinh lớp 6 đến lớp 12",
        "instructor": "Thầy Lê Văn Thông và đội ngũ giảng dạy",
        "eligibility_q": "Học sinh lớp nào có thể đăng ký?",
        "eligibility_a": "Trung tâm nhận học sinh từ lớp 6 đến lớp 12, xếp lớp theo năng lực thực tế.",
        "teacher_bio": "",
        "subject_image": '<img src="/assets/images/thay-thong-lop-vatly-01.jpg" alt="Thầy Lê Văn Thông cùng học sinh lớp Vật lý" class="rounded-xl mt-6 w-full h-auto object-cover aspect-video">',
    },
    "anhvan": {
        "name": "Anh văn",
        "title_suffix": "(Lớp 6–12)",
        "summary": "Chương trình Anh văn từ lớp 6 đến lớp 12, phát triển toàn diện 4 kỹ năng và luyện thi.",
        "levels": GRADE_LEVELS,
        "level_col_header": "Khối lớp",
        "focus": {
            "Lớp 6": "Ngữ pháp nền tảng, từ vựng chủ đề quen thuộc",
            "Lớp 7": "Mở rộng vốn từ, các thì cơ bản",
            "Lớp 8": "Ngữ pháp nâng cao, kỹ năng đọc hiểu",
            "Lớp 9": "Ôn thi vào lớp 10: ngữ pháp trọng tâm, luyện đề",
            "Lớp 10": "Củng cố ngữ pháp, kỹ năng viết đoạn văn",
            "Lớp 11": "Từ vựng học thuật, kỹ năng đọc hiểu nâng cao",
            "Lớp 12": "Ôn thi THPT: luyện đề, chiến lược làm bài trắc nghiệm",
        },
        "audience": "Học sinh lớp 6 đến lớp 12",
        "instructor": "Thầy Lê Văn Thông, thầy Lê Hồng Trân và đội ngũ giảng dạy",
        "eligibility_q": "Học sinh lớp nào có thể đăng ký?",
        "eligibility_a": "Trung tâm nhận học sinh từ lớp 6 đến lớp 12, xếp lớp theo năng lực thực tế.",
        "teacher_bio": "Thầy Lê Hồng Trân hiện là nghiên cứu sinh tiến sĩ tại Học viện Công nghệ Châu Á AIT (Thái Lan). Thầy từng giảng dạy tại Đại học Khoa học Ứng dụng NHL Stenden (Hà Lan), đồng thời là giảng viên tại Đại học Kinh tế TP.HCM và Trường Đại học Khoa học Xã hội và Nhân văn. Với nền tảng học thuật quốc tế, thầy đưa phương pháp giảng dạy tiên tiến, kết hợp kinh nghiệm thực tiễn từ môi trường giáo dục trong và ngoài nước đến với học sinh của trung tâm.",
        "subject_image": '<img src="/assets/images/student-english-study.jpg" alt="Học sinh học Anh văn tại trung tâm" class="rounded-xl mt-6 w-full h-auto object-cover aspect-video">',
    },
    "ielts": {
        "name": "IELTS",
        "title_suffix": "(Band 5.0–6.5)",
        "summary": "Luyện thi IELTS từ Band 5.0 đến Band 6.5, do Thầy Lê Hồng Trân trực tiếp phụ trách.",
        "levels": IELTS_LEVELS,
        "level_col_header": "Trình độ mục tiêu",
        "focus": {
            "Band 5.0": "Củng cố nền tảng 4 kỹ năng, từ vựng và ngữ pháp cốt lõi",
            "Band 5.5": "Phát triển kỹ năng làm bài theo từng dạng đề, mở rộng từ vựng học thuật",
            "Band 6.0": "Nâng cao kỹ năng Writing Task 1 & 2, Speaking theo chủ đề học thuật",
            "Band 6.5": "Luyện đề chuyên sâu, chiến lược làm bài tốc độ và độ chính xác cao",
        },
        "audience": "Học sinh có nhu cầu luyện thi IELTS từ trình độ Band 5.0 đến 6.5",
        "instructor": "Thầy Lê Hồng Trân",
        "eligibility_q": "Học sinh trình độ nào có thể đăng ký?",
        "eligibility_a": "Trung tâm nhận học sinh từ Band 5.0 đến Band 6.5, được tư vấn trực tiếp để xếp lớp phù hợp với năng lực hiện tại.",
        "teacher_bio": "Thầy hiện là nghiên cứu sinh tiến sĩ tại Học viện Công nghệ Châu Á AIT (Thái Lan). Thầy từng giảng dạy tại Đại học Khoa học Ứng dụng NHL Stenden (Hà Lan), đồng thời là giảng viên tại Đại học Kinh tế TP.HCM và Trường Đại học Khoa học Xã hội và Nhân văn. Với nền tảng học thuật quốc tế, thầy đưa phương pháp giảng dạy tiên tiến, kết hợp kinh nghiệm thực tiễn từ môi trường giáo dục trong và ngoài nước đến với học sinh của trung tâm.",
        "subject_image": "",
    },
}

def subject_page(slug):
    cfg = SUBJECTS[slug]
    name = cfg["name"]
    summary = cfg["summary"]
    title_suffix = cfg["title_suffix"]
    focus = cfg["focus"]

    other_subjects = [(s, c["name"], c["title_suffix"]) for s, c in SUBJECTS.items() if s != slug]
    related_html = "\n        ".join(
        f'<a href="/programs/{r_slug}.html" class="border rounded-lg px-4 py-2 text-sm font-medium text-[--color-primary] hover:bg-gray-50">{r_name} {r_suffix}</a>'
        for r_slug, r_name, r_suffix in other_subjects
    )

    teacher_bio_html = f'<p class="text-gray-600 mt-1">{cfg["teacher_bio"]}</p>' if cfg["teacher_bio"] else ""

    body = f"""  <main class="max-w-4xl mx-auto px-4 py-10">
    <h1 class="text-3xl font-bold text-[--color-primary]">Khóa {name} {title_suffix}</h1>
    <p class="mt-3 text-gray-600">{summary}</p>
    {cfg["subject_image"]}

    <div class="mt-8 grid sm:grid-cols-2 gap-4 text-sm">
      <div class="border rounded-xl p-4"><p class="font-semibold text-[--color-primary]">Đối tượng học sinh</p><p class="text-gray-600 mt-1">{cfg["audience"]}</p></div>
      <div class="border rounded-xl p-4"><p class="font-semibold text-[--color-primary]">Sĩ số lớp</p><p class="text-gray-600 mt-1">Tối đa {CLASS_SIZE} học sinh</p></div>
      <div class="border rounded-xl p-4"><p class="font-semibold text-[--color-primary]">Giảng viên</p><p class="text-gray-600 mt-1">{cfg["instructor"]}</p>{teacher_bio_html}</div>
    </div>

    <div class="mt-10 text-center">
      <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="inline-block bg-[--color-accent] text-[--color-primary] font-bold px-8 py-3 rounded-full">Tư vấn qua Zalo</a>
    </div>

    <div class="mt-10">
      <h2 class="text-xl font-bold text-[--color-primary] mb-3">Khóa học khác</h2>
      <div class="flex flex-wrap gap-3">
        {related_html}
      </div>
    </div>
  </main>
"""
    write(f"programs/{slug}.html", page(
        f"Khóa {name} {title_suffix} | {CENTER_NAME}", summary, f"/programs/{slug}.html", body, asset_prefix="../"))

for slug in SUBJECTS:
    subject_page(slug)

# ---------- about.html ----------
about_body = f"""  <main class="max-w-4xl mx-auto px-4 py-10">
    <div class="text-center">
      <img src="/assets/images/teacher-whiteboard.jpg" alt="Thầy Lê Văn Thông" class="w-48 h-48 mx-auto rounded-full object-cover">
      <h1 class="text-3xl font-bold text-[--color-primary] mt-4">Thầy Lê Văn Thông</h1>
      <p class="text-gray-600">Nhiều năm kinh nghiệm dạy luyện thi Đại học, sáng lập trung tâm</p>
    </div>

    <img src="/assets/images/thay-thong-lop-vatly-02.jpg" alt="Thầy Lê Văn Thông cùng học sinh" class="rounded-xl mt-8 w-full h-auto object-cover aspect-video">

    <div class="mt-8">
      <h2 class="text-xl font-bold text-[--color-primary]">Tiểu sử</h2>
      <ul class="mt-3 text-gray-600 space-y-1 text-sm list-disc list-inside">
        <li>Nhiều năm kinh nghiệm dạy luyện thi Đại học</li>
        <li>Giáo viên dạy luyện thi đại học tại  các trung tâm của Đại học Bách Khoa & Đại học Kinh tế TP.HCM, Trung tâm Tân Lê Hồng Phong, chương trình luyện thi đại học của Đài truyền hình HTV4 và Trường BDVH 218 Lý Tự Trọng</li>
        <li>Tác giả của hơn 40 bộ sách được xuất bản trên quy mô cả nước</li>
        <li>Triết lý giảng dạy: mỗi học sinh một lộ trình riêng, không rập khuôn. Thầy đồng hành sát sao cùng học sinh trên từng chặng đường, từ nền tảng đến khi vững vàng chinh phục mục tiêu đại học</li>
      </ul>
    </div>

    <div class="mt-8">
      <h2 class="text-xl font-bold text-[--color-primary]">Tài liệu / Ấn phẩm tiêu biểu</h2>
      <p class="mt-2 text-sm text-gray-600">Thầy là tác giả của hơn 40 bộ sách được xuất bản trên quy mô cả nước.</p>
      <div class="mt-3 grid sm:grid-cols-2 md:grid-cols-4 gap-4 text-sm">
        <img src="/assets/images/sach-vatly-11.jpg" alt="Sách Phân loại và phương pháp giải bài tập Vật Lí 11, tác giả Lê Văn Thông" class="rounded-xl w-full h-auto object-cover">
        <img src="/assets/images/sach-vatly-01.jpg" alt="Sách Tuyển tập các bài toán Vật Lý - Luyện thi đại học, tác giả Lê Văn Thông" class="rounded-xl w-full h-auto object-cover">
        <img src="/assets/images/sach-vatly-02.jpg" alt="Sách Phân loại và phương pháp giải bài tập Vật Lí 10, tác giả Lê Văn Thông" class="rounded-xl w-full h-auto object-cover">
        <img src="/assets/images/sach-vatly-03.jpg" alt="Sách Tuyển chọn những bài toán trong các đề thi đại học & cao đẳng Vật Lý 12, tác giả Lê Văn Thông" class="rounded-xl w-full h-auto object-cover">
      </div>
    </div>

    <div class="mt-8">
      <h2 class="text-xl font-bold text-[--color-primary]">Vì sao học sinh chọn trung tâm</h2>
      <div class="mt-3 grid sm:grid-cols-2 gap-4 text-sm">
        <div class="border rounded-xl p-4 text-gray-600">"Thầy luôn đồng hành cùng con qua từng giai đoạn ôn thi, không chỉ dạy kiến thức mà còn giúp con vững tâm lý để vươn tới mục tiêu đại học."</div>
        <div class="border rounded-xl p-4 text-gray-600">"Lớp học nhỏ nên Thầy sát sao từng học sinh, kèm cặp tận tâm như một người đồng hành thực sự trên chặng đường học tập."</div>
        <div class="border rounded-xl p-4 text-gray-600">"Nhờ sự dìu dắt bền bỉ của Thầy suốt nhiều năm, con tôi đã tự tin và vững vàng hơn rất nhiều trên con đường chinh phục đại học."</div>
        <div class="border rounded-xl p-4 text-gray-600">"Thầy không chỉ là người dạy học mà còn là người đồng hành, luôn động viên và giúp em giữ vững mục tiêu dài hạn."</div>
      </div>
    </div>

    <div class="mt-10 text-center">
      <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="inline-block bg-[--color-accent] text-[--color-primary] font-bold px-8 py-3 rounded-full">Tư vấn qua Zalo</a>
    </div>
  </main>
"""
write("about.html", page("Thầy Lê Văn Thông | " + CENTER_NAME, "Thầy Lê Văn Thông: nhiều năm kinh nghiệm dạy luyện thi Đại học, tác giả hơn 40 bộ sách được xuất bản trên quy mô cả nước.", "/about.html", about_body))

# ---------- method.html ----------
method_body = """  <main class="max-w-4xl mx-auto px-4 py-10">
    <h1 class="text-3xl font-bold text-[--color-primary]">Phương pháp học</h1>
    <p class="mt-3 text-gray-600">[ Mô tả tổng quan về phương pháp giảng dạy của trung tâm ]</p>

    <div class="mt-8 grid sm:grid-cols-2 gap-6">
      <div class="border rounded-xl p-5">
        <h2 class="font-bold text-[--color-primary]">1. Tư vấn & xác định mục tiêu</h2>
        <p class="text-sm text-gray-600 mt-2">[ Mô tả bước trao đổi với phụ huynh/học sinh để hiểu năng lực và mục tiêu, không cần bài kiểm tra đầu vào ]</p>
      </div>
      <div class="border rounded-xl p-5">
        <h2 class="font-bold text-[--color-primary]">2. Lộ trình cá nhân hóa</h2>
        <p class="text-sm text-gray-600 mt-2">[ Mô tả cách xây dựng lộ trình riêng cho từng học sinh ]</p>
      </div>
      <div class="border rounded-xl p-5">
        <h2 class="font-bold text-[--color-primary]">3. Lớp học sĩ số ít</h2>
        <p class="text-sm text-gray-600 mt-2">[ Mô tả lợi ích của lớp học nhỏ ]</p>
      </div>
      <div class="border rounded-xl p-5">
        <h2 class="font-bold text-[--color-primary]">4. Theo dõi tiến độ hàng tuần</h2>
        <p class="text-sm text-gray-600 mt-2">[ Mô tả cách báo cáo tiến độ cho phụ huynh ]</p>
      </div>
    </div>

    <div class="mt-10 text-center">
      <a href="/assessment.html" class="inline-block bg-[--color-accent] text-[--color-primary] font-bold px-8 py-3 rounded-full">Nhận lộ trình cá nhân hóa</a>
    </div>
  </main>
"""
write("method.html", page("Phương pháp học | " + CENTER_NAME, "Phương pháp giảng dạy cá nhân hóa, không cần kiểm tra đầu vào, theo dõi tiến độ hàng tuần.", "/method.html", method_body))

# ---------- assessment.html ----------
assessment_body = f"""  <main class="max-w-2xl mx-auto px-4 py-10">
    <h1 class="text-3xl font-bold text-[--color-primary] text-center">Tư vấn miễn phí</h1>
    <p class="mt-3 text-gray-600 text-center">Không cần làm bài kiểm tra đầu vào — chỉ cần điền thông tin bên dưới, đội ngũ trung tâm sẽ liên hệ tư vấn lộ trình trong 15 phút.</p>

    <form id="assessment-form" data-endpoint="{FORM_ENDPOINT}" class="mt-8 space-y-4 bg-white border rounded-xl p-6">
      <div>
        <label class="block text-sm font-medium mb-1" for="student-name">Họ tên học sinh *</label>
        <input id="student-name" name="studentName" type="text" required class="w-full border rounded-lg px-3 py-2">
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="grade">Lớp *</label>
        <select id="grade" name="grade" required class="w-full border rounded-lg px-3 py-2">
          <option value="">-- Chọn lớp --</option>
          {"".join(f'<option value="{g}">Lớp {g}</option>' for g in GRADES)}
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="school">Trường</label>
        <input id="school" name="school" type="text" class="w-full border rounded-lg px-3 py-2">
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="phone">Số điện thoại phụ huynh *</label>
        <input id="phone" name="parentPhone" type="tel" required pattern="^(0|\\+84)[0-9]{{9}}$" placeholder="0901234567" class="w-full border rounded-lg px-3 py-2">
      </div>
      <div>
        <span class="block text-sm font-medium mb-1">Môn cần học</span>
        <div class="flex flex-wrap gap-4 text-sm">
          <label class="flex items-center gap-2"><input type="checkbox" name="subjects" value="Toán"> Toán</label>
          <label class="flex items-center gap-2"><input type="checkbox" name="subjects" value="Vật lý"> Vật lý</label>
          <label class="flex items-center gap-2"><input type="checkbox" name="subjects" value="Anh văn"> Anh văn</label>
          <label class="flex items-center gap-2"><input type="checkbox" name="subjects" value="IELTS"> IELTS</label>
        </div>
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="target">Ghi chú thêm (nếu có)</label>
        <input id="target" name="target" type="text" class="w-full border rounded-lg px-3 py-2">
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="contact-time">Thời gian liên hệ thuận tiện</label>
        <select id="contact-time" name="contactTime" class="w-full border rounded-lg px-3 py-2">
          <option value="Sáng">Sáng</option>
          <option value="Chiều">Chiều</option>
          <option value="Tối">Tối</option>
        </select>
      </div>
      <button id="assessment-submit-btn" type="submit" class="w-full bg-[--color-accent] text-[--color-primary] font-bold py-3 rounded-full">Đăng ký ngay</button>
      <p id="assessment-form-error" class="text-sm text-red-600 text-center hidden">Có lỗi xảy ra, vui lòng thử lại hoặc gọi trực tiếp {PHONE_DISPLAY}.</p>
      <p class="text-xs text-gray-400 text-center">Thông tin của bạn chỉ dùng để liên hệ tư vấn, không chia sẻ cho bên thứ ba.</p>
    </form>

    <div id="assessment-success" class="mt-8 bg-white border rounded-xl p-6 text-center hidden">
      <p class="text-xl font-bold text-[--color-primary]">Cảm ơn bạn đã đăng ký!</p>
      <p class="mt-2 text-gray-600">Đội ngũ trung tâm sẽ liên hệ tư vấn trong 15 phút. Bạn cũng có thể chủ động nhắn Zalo để được hỗ trợ nhanh hơn.</p>
      <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="inline-block mt-4 bg-[--color-primary] text-white font-semibold px-6 py-3 rounded-full">Nhắn tin Zalo ngay</a>
    </div>
  </main>
"""
write("assessment.html", page("Tư vấn miễn phí | " + CENTER_NAME, "Đăng ký tư vấn lộ trình miễn phí cho khóa Toán, Vật lý, Tiếng Anh tại LêVănThông Education, không cần làm bài kiểm tra đầu vào.", "/assessment.html", assessment_body))

# ---------- results.html (Gương sáng) ----------
results_body = f"""  <main class="max-w-5xl mx-auto px-4 py-10">
    <h1 class="text-3xl font-bold text-[--color-primary] text-center">Gương sáng</h1>
    <p class="mt-3 text-gray-600 text-center">Những học sinh đã trưởng thành từ lớp học của Thầy.</p>

    <div class="mt-8 border rounded-xl overflow-hidden sm:grid sm:grid-cols-2">
      <img src="/assets/images/guong-sang-phan-hai-anh.jpg" alt="Thầy Lê Văn Thông cùng học sinh Phan Hải Anh" class="w-full h-full object-cover">
      <div class="p-6">
        <h2 class="text-xl font-bold text-[--color-primary]">Phan Hải Anh</h2>
        <p class="mt-3 text-gray-600 text-sm">Chúc mừng em Phan Hải Anh đã xuất sắc được tuyển thẳng vào cả hai trường đại học năm 2026:</p>
        <ul class="mt-2 text-gray-600 text-sm list-disc list-inside space-y-1">
          <li>Học viện Ngoại giao</li>
          <li>Trường Đại học Khoa học Xã hội và Nhân văn</li>
        </ul>
        <p class="mt-3 text-gray-600 text-sm">Mới ngày nào em còn là cậu học trò nhỏ, bỡ ngỡ bước vào lớp dạy kèm của thầy từ năm lớp 9 học liên tục đến lớp 12. Hôm nay, bằng sự chăm chỉ, nỗ lực và quyết tâm, em đã gặt hái được thành quả thật đáng tự hào.</p>
        <p class="mt-3 text-gray-600 text-sm">Niềm vui này không chỉ của riêng em mà còn là niềm hạnh phúc của gia đình, thầy cô và những người luôn dõi theo em.</p>
        <p class="mt-3 text-gray-600 text-sm">Chúc em vững bước trên chặng đường đại học, tiếp tục nuôi dưỡng ước mơ, gặt hái nhiều thành công và trở thành phiên bản tốt đẹp nhất của chính mình.</p>
      </div>
    </div>

    <h2 class="mt-12 text-2xl font-bold text-center text-[--color-primary]">Chia sẻ của học sinh và phụ huynh</h2>
    <div class="mt-6 grid sm:grid-cols-2 md:grid-cols-3 gap-6">
""" + "\n".join(f"""      <div class="border rounded-xl p-5">
        <div class="w-14 h-14 rounded-full bg-gray-200 mb-3"></div>
        <p class="text-sm text-gray-600">"{quote}"</p>
        <p class="mt-2 text-sm font-semibold text-gray-800">{who}</p>
      </div>""" for quote, who in [
    ("Thầy đồng hành cùng con suốt hành trình ôn thi, không chỉ dạy kiến thức mà còn giúp con giữ vững mục tiêu vào đại học.", "Phụ huynh học sinh lớp 12"),
    ("Nhờ sự kèm cặp sát sao của Thầy qua từng buổi học, em đã tự tin hơn rất nhiều khi bước vào kỳ thi đại học.", "Cựu học sinh"),
    ("Lớp học nhỏ, Thầy luôn theo sát và động viên kịp thời, giúp con vững tâm lý trên chặng đường dài chinh phục đại học.", "Phụ huynh học sinh"),
    ("Thầy như người đồng hành thực sự, luôn kiên trì dìu dắt em qua những giai đoạn khó khăn nhất trong quá trình ôn tập.", "Học sinh lớp 12"),
    ("Con tôi tiến bộ rõ rệt sau mỗi tháng học, quan trọng hơn là con luôn giữ được động lực nhờ sự đồng hành của Thầy.", "Phụ huynh học sinh"),
    ("Không chỉ ôn kiến thức, Thầy còn giúp em xây dựng lộ trình rõ ràng để từng bước vươn tới mục tiêu đại học.", "Học sinh lớp 11"),
    ("Sự tận tâm và kiên nhẫn của Thầy là điều khiến gia đình tôi luôn yên tâm gửi gắm con trong suốt nhiều năm.", "Phụ huynh học sinh"),
    ("Em biết ơn Thầy vì đã đồng hành cùng em không chỉ trong học tập mà cả những lúc em mất phương hướng với mục tiêu của mình.", "Cựu học sinh"),
]) + f"""
    </div>
    <div class="mt-10 text-center">
      <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="inline-block bg-[--color-accent] text-[--color-primary] font-bold px-8 py-3 rounded-full">Tư vấn qua Zalo</a>
    </div>
  </main>
"""
write("results.html", page("Gương sáng | " + CENTER_NAME, "Những học sinh đã trưởng thành từ lớp học của Thầy Lê Văn Thông, cùng kết quả và cảm nhận từ học sinh, phụ huynh.", "/results.html", results_body))

# ---------- public-info.html ----------
public_info_body = f"""  <main class="max-w-3xl mx-auto px-4 py-10">
    <h1 class="text-3xl font-bold text-[--color-primary]">Thông tin công khai</h1>
    <div class="mt-6 space-y-4 text-sm text-gray-600">
      <p><strong>Tên trung tâm:</strong> {CENTER_NAME}</p>
      <p><strong>Địa chỉ:</strong> {ADDRESS}</p>
      <p><strong>Điện thoại:</strong> {PHONE_DISPLAY}</p>
      <p><strong>Giờ hoạt động:</strong> 8:00 – 21:00, Thứ 2 – Chủ nhật</p>
      <p><strong>Giấy phép hoạt động:</strong> [ Số giấy phép / cơ quan cấp phép ]</p>
      <p><strong>Người đại diện:</strong> [ Tên người đại diện pháp lý ]</p>
    </div>
  </main>
"""
write("public-info.html", page("Thông tin công khai | " + CENTER_NAME, "Thông tin công khai, giấy phép hoạt động của trung tâm Thầy Lê Văn Thông.", "/public-info.html", public_info_body))

# ---------- contact.html ----------
contact_body = f"""  <main class="max-w-4xl mx-auto px-4 py-10">
    <h1 class="text-3xl font-bold text-[--color-primary]">Liên hệ</h1>
    <div class="mt-6 grid sm:grid-cols-2 gap-8">
      <div>
        <div class="aspect-video rounded-xl overflow-hidden">{MAP_IFRAME}</div>
        <a href="https://www.google.com/maps/dir/?api=1&destination={ADDRESS.replace(' ', '+')}" target="_blank" rel="noopener" class="inline-block mt-3 text-[--color-primary] font-semibold underline">Chỉ đường &rarr;</a>
      </div>
      <div class="space-y-3 text-sm">
        <p><strong>Địa chỉ:</strong> {ADDRESS}</p>
        <p><strong>Điện thoại:</strong> <a href="{PHONE_TEL}" class="text-[--color-primary] font-semibold">{PHONE_DISPLAY}</a></p>
        <p><strong>Zalo:</strong> {PHONE_TEL.replace('tel:', '')} <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="text-[--color-primary] font-semibold">Nhắn tin Zalo</a></p>
        <p><strong>Giờ hoạt động:</strong> 8:00 – 21:00, Thứ 2 – Chủ nhật</p>
      </div>
    </div>
    <div class="mt-10 text-center">
      <a href="{ZALO_LINK}" target="_blank" rel="noopener" class="inline-block bg-[--color-accent] text-[--color-primary] font-bold px-8 py-3 rounded-full">Tư vấn qua Zalo</a>
    </div>
  </main>
"""
write("contact.html", page("Liên hệ | " + CENTER_NAME, f"Liên hệ trung tâm Thầy Lê Văn Thông tại {ADDRESS}.", "/contact.html", contact_body))

print("Done.")
