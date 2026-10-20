# JUST FOR YOU — 20/10 ♡

Website quà tặng Rem của Bon. Một trải nghiệm **Cinematic Fullscreen**, viết bằng **một file HTML chứa toàn bộ CSS và JavaScript**, kết hợp thư mục tài nguyên (ảnh / âm thanh / video). **Không cần backend, database, tài khoản hay công cụ build.**

## Lưu ý khi nâng cấp từ bản cũ

Nếu bạn **đã tự chỉnh `index.html`**, đừng chép đè file của mình bằng bản V2 vì sẽ mất những sửa đổi riêng. Chỉ cần:

1. Chép hai file mới `assets/audio/quiz-playful.mp3` và `assets/audio/letter.mp3` vào thư mục dự án cũ của bạn.
2. Trong `CONFIG.audio`, thêm `quiz: 'assets/audio/quiz-playful.mp3'` (giữ nguyên những bài nhạc bạn đã tự sửa).
3. Tìm hàm `musicForStage(stage)` và sửa theo đoạn mã V2, để nhạc chạy ở màn 2 và màn 4.
4. Nếu thích, sao chép phần điều chỉnh âm lượng và `catSound` trong `index.html` V2 để tiếng mèo nổi bật hơn.

Nếu chưa từng chỉnh code, dùng trọn bộ V2 là cách đơn giản nhất.

## 1. Xem thử ngay trên máy (Windows)

1. Giải nén `20-10-just-for-rem-v2.zip` bằng **Extract All...**.
2. Mở thư mục vừa giải nén.
3. **Nhấp đúp `index.html`**, Chrome hoặc Edge sẽ mở website.
4. Nhấn **Mở món quà này** để bắt đầu. Quiz 1 và Quiz 2 dùng đáp án bạn đã định; nhạc quiz và thư đã có sẵn, nhưng ảnh / nhạc recap / nhạc cuối / video cần bạn tự thêm.
5. Khi chưa thêm ảnh, recap hiện nền chữ nghệ thuật thay thế. Nếu thiếu video, màn video có nút **Xem đoạn kết** để kiểm tra trước. Các hiệu ứng mèo tổng hợp (`cat-correct.wav` và `cat-wrong.wav`) đã được kèm sẵn.

> Chạy bằng file HTML local hoạt động được với các ảnh và âm thanh đặt trong thư mục `assets/` bên cạnh file HTML. Font chữ có thể hơi khác khi offline vì có dùng Google Fonts với font hệ thống dự phòng.

## 2. Thêm ảnh buổi hẹn 20/10

Thả ảnh của hai bạn vào thư mục **`assets/photos/`** và đặt tên như sau:

| Ảnh | Đường dẫn |
|---|---|
| 1 | `assets/photos/photo-01.jpg` |
| 2 | `assets/photos/photo-02.jpg` |
| 3 | `assets/photos/photo-03.jpg` |
| 4 | `assets/photos/photo-04.jpg` |
| 5 | `assets/photos/photo-05.jpg` |
| 6 | `assets/photos/photo-06.jpg` |

- Dùng JPG/JPEG để giữ đúng cấu hình sẵn. Nếu ảnh là PNG, WebP hoặc tên khác, có thể đổi đường dẫn tại `CONFIG.recap.slides`.
- Ảnh được trình bày **toàn màn hình** và dùng `object-fit: cover` nên có thể bị cắt rìa ở một số tỷ lệ màn hình. Ưu tiên ảnh dọc hoặc ảnh có nhân vật ở trung tâm để xem bằng điện thoại.
- Khuyến nghị mỗi ảnh khoảng 200–800 KB (đã nén), độ phân giải 1200–2000 px ở cạnh dài tùy ảnh.
- Mỗi slide có các thuộc tính `image`, `title`, `italic`, `description`, `placeholder`. Bạn có thể thay chú thích, thêm hoặc bớt slide trong mảng `CONFIG.recap.slides`.

## 3. Nhạc nền và âm thanh — đã thêm cho quiz & bức thư

**V2 đã có nhạc nền thật** ở 2 quiz và bức thư: không cần tự tìm/tải nhạc nếu bạn thích 2 giai điệu tặng kèm. Hai file là giai điệu gốc được tạo riêng cho website, không phải bài hát thương mại:

| Phần | Bản nhạc | File | Có sẵn? |
|---|---|---|---|
| Quiz 1 & Quiz 2 | **Playful Little Cat** — giai điệu tinh nghịch, đàn gảy và tiếng chuông | `assets/audio/quiz-playful.mp3` | **Có** |
| Recap | **Until You — Shayne Ward** | `assets/audio/until-you-shayne-ward.mp3` | **Chưa, tự thêm** |
| Bức thư | **A Little Letter** — bản piano gốc lãng mạn, dịu dàng | `assets/audio/letter.mp3` | **Có** |
| Video | Tiếng trong video | `assets/video/message.mp4` | Tự thêm |
| Hoa nở cuối | **I Do — 911** | `assets/audio/i-do-911.mp3` | **Chưa, tự thêm** |

Hai bài thương mại (Until You, I Do) **không đính kèm**. Bạn tự cung cấp MP3 có quyền sử dụng và chép đúng tên vào `assets/audio/`.

**Quiz:** Nhạc bắt đầu khi bạn bấm vào trang quiz, dừng khi chuyển sang lời mời, rồi phát lại ở quiz thứ 2. Khi trả lời đúng/sai, tiếng mèo vẫn vang lên và âm lượng nhạc nền được hạ tạm thời. Hai âm thanh mèo đã có sẵn: `cat-wrong.wav`, `cat-correct.wav` (âm thanh mô phỏng được tổng hợp, không phải tiếng mèo ghi âm).

**Thư:** Piano tự phát lúc chuyển vào màn thư (nếu trình duyệt cho phép), lặp cho đến khi bạn sang video. Nhạc sẽ dừng khi xem video. Để thay bài khác, chép một MP3 tên `letter.mp3` lên file cũ, hoặc sửa `CONFIG.audio.letter`.

**Thay nhạc quiz:** Bạn có thể thay `assets/audio/quiz-playful.mp3` bằng bản nhạc ưa thích, hoặc sửa `CONFIG.audio.quiz` sang đường dẫn mới. Muốn bỏ nhạc quiz, sửa `quiz: ''`.

> Các trình duyệt trên điện thoại đôi khi chặn phát nhạc tự động. Nút âm thanh ở góc có thể tắt/bật lại để phát nhạc. Website không thể vượt qua giới hạn autoplay của trình duyệt bằng mã JavaScript thuần.

## 4. Thêm video bạn quay

1. Xuất video dưới dạng **MP4 (H.264 cho hình và AAC cho tiếng)** để có tính tương thích cao trên Chrome/Edge/Safari/mobile.
2. Đặt tên chính xác `message.mp4`.
3. Chép file vào: **`assets/video/message.mp4`**.
4. Khi người xem đến màn video, nhấn **Play**. Video chạy với nút điều khiển mặc định. **Kết thúc tự động** chuyển qua màn hoa nở và chữ **Anh yêu em.**

Khuyên dùng video 720p hoặc 1080p vừa phải. Khi tải video lên GitHub bằng **giao diện web**, GitHub giới hạn 25 MiB/tệp; bạn có thể nén video nhỏ hơn giới hạn này để tải thuận tiện, hoặc dùng Git/GitHub Desktop nếu file lớn hơn (GitHub có các giới hạn file khác). Không đưa video quá lớn lên Pages vì sẽ tải chậm trên 4G.

## 5. Sửa câu chữ, lời mời và bức thư

Khuyến nghị mở `index.html` bằng [Visual Studio Code](https://code.visualstudio.com/) (miễn phí). Trong file:

1. Nhấn `Ctrl + F`, tìm **`const CONFIG = {`**.
2. **Quiz 1:** `CONFIG.quiz1.answer` đang là `Bon`. Không phân biệt hoa/thường và ô nhập chỉ có placeholder trung tính. Ba câu hỏi gốc nằm trong HTML.
3. **Quiz 2:** `CONFIG.quiz2.answer` đang là `14/1/2026`. Chấp nhận cả `14/01/2026` (và số 0 thêm trước tháng/ngày).
4. **Lời mời:** sửa `CONFIG.invitation.title` và `CONFIG.invitation.body`.
5. **Recap:** sửa `CONFIG.recap.slides` để thay ảnh, tiêu đề, caption.
6. **Bức thư:** sửa `CONFIG.letter.greeting`, `CONFIG.letter.pages`, `CONFIG.letter.signature`. Mỗi phần tử trong `pages` là **một trang riêng**; giữ mỗi trang 2–4 câu để vừa màn hình điện thoại.
7. **Nhạc:** `CONFIG.audio.quiz`, `.recap`, `.letter`, `.finale` là đường dẫn MP3.
8. **Video:** `CONFIG.video` là đường dẫn MP4.

**Ví dụ cách sửa một đoạn thư:**

```js
letter: {
  greeting: 'Rem yêu của anh,',
  signature: '— Bon ♡',
  pages: [
    'Đoạn thứ nhất anh muốn gửi em...',
    'Đoạn thứ hai chứa một kỷ niệm...',
    'Đoạn kết với lời chúc thật đặc biệt...'
  ]
},
```

**Lưu ý:** Trong JavaScript, nếu lời nhắn nằm giữa dấu nháy đơn `'...'` thì dấu nháy đơn bên trong câu cần được thoát bằng `\'` hoặc đổi sang nháy kép `"..."`. Sau khi chỉnh, nhấn **Ctrl+S**, sau đó reload trang (Ctrl+R).

## 6. Đưa website lên GitHub Pages, từng bước

### 6A. Chuẩn bị repository

1. Tạo/đăng nhập tài khoản GitHub: https://github.com/.
2. Bấm dấu **+** góc trên bên phải → **New repository**.
3. Đặt tên ví dụ `just-for-rem-2010` (chỉ là ví dụ; bạn chọn tên khác cũng được).
4. Chọn **Public** nếu dùng GitHub Free thông thường để chạy Pages miễn phí; trang Pages là public, các tài nguyên cũng truy cập được nếu ai biết link.
5. Bấm **Create repository**.

### 6B. Đưa các file lên

1. **Giải nén ZIP** trước. **Không** tải cả ZIP vào repo và mong Pages tự giải nén.
2. Trong trang repo, chọn **Add file → Upload files**.
3. Tải `index.html` và toàn bộ thư mục `assets` (gồm `photos`, `audio`, `video`) lên. Kèm `README.md` nếu muốn. Một số trình duyệt cho phép kéo cả thư mục vào giao diện upload; nếu không thì dùng **GitHub Desktop** để commit cả cấu trúc thư mục, hoặc tạo các đường dẫn thư mục trên web.
4. Kiểm tra trong repo có đường dẫn `index.html` **ở gốc repository**, **không** nằm trong một thư mục con `20-10-just-for-rem/`.
5. Kéo xuống và bấm **Commit changes**.

### 6C. Bật GitHub Pages

1. Vào trang repo → **Settings**.
2. Ở menu bên trái, vào **Pages**.
3. Trong **Build and deployment**, chọn **Source → Deploy from a branch**.
4. Ở **Branch**, chọn `main`; ở thư mục chọn `/(root)`.
5. Bấm **Save**.
6. Chờ GitHub triển khai (có thể mất vài phút, tài liệu GitHub nói tối đa khoảng 10 phút cho các thay đổi).
7. Vẫn trong **Settings → Pages**, bấm **Visit site**, hoặc truy cập theo mẫu:

   `https://TEN_TAI_KHOAN.github.io/just-for-rem-2010/`

   Thay `TEN_TAI_KHOAN` và tên repo bằng thông tin thực tế của bạn.

Tài liệu GitHub chính thức:
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

### 6D. Khi cần chỉnh sửa sau khi đăng

Chỉnh `index.html` trên VS Code (hoặc GitHub Edit), thêm ảnh/nhạc/video vào repo, rồi **Commit changes**. Pages sẽ tự cập nhật sau khi triển khai thành công. Có thể cần hard-refresh trình duyệt để thấy bản mới.

## 7. Trước khi gửi link cho Rem — Checklist

- [ ] Có ảnh thật trong các slide recap; ảnh không vỡ, không che mặt trên mobile.
- [ ] Đã chép `until-you-shayne-ward.mp3` và `i-do-911.mp3` đúng chỗ.
- [ ] Đã thử nhạc quiz vui nhộn và piano bức thư (hoặc thay bài theo ý thích).
- [ ] Đã thay **lời mời** bằng câu chữ bạn muốn.
- [ ] Đã thay **3 trang thư mẫu** thành lời nhắn thật của bạn.
- [ ] Đã chép và test `message.mp4` trên cả điện thoại và máy tính.
- [ ] Đã thử Quiz 1 cả `Bon`, `bon`, `bOn`; thử Quiz 2 cả `14/1/2026`, `14/01/2026`.
- [ ] Đã thử bật/tắt nhạc, xem hết video, xem hoa nở và phát bài cuối.
- [ ] Link Pages hoạt động khi mở trong tab ẩn danh hoặc thiết bị khác.

## 8. Ghi chú về riêng tư và giới hạn

Website **không thu thập hay gửi câu trả lời** của người xem về máy chủ nào. Mọi xử lý chạy trong trình duyệt; quiz chỉ nhằm tạo tương tác, **không phải cơ chế bảo vệ dữ liệu**. Nếu công khai GitHub Pages thì người biết link hoặc xem source có thể truy cập ảnh, video, thư, đáp án quiz. Hãy cân nhắc trước khi đăng nội dung riêng tư.

Nếu website thiếu tệp âm thanh, phần đó sẽ chạy trong im lặng hoặc hiện một thông báo nhỏ, không làm sập trải nghiệm. Nếu chưa có video, nút xem thử ending hiện ra để bạn kiểm tra hiệu ứng cuối.

---

**Project:** 20.10 — Just for You ♡ | **Made with love, by Bon**
