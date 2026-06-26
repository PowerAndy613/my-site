# Run Python on iPhone via GitHub Pages (Pyodide)

說明
- 使用 Pyodide（CPython via WebAssembly）在瀏覽器中執行 Python，無需伺服器。
- 把此 repo 啟用 GitHub Pages（或將檔案放到 /docs 並啟用 Pages）後，使用 iPhone 的 Safari 打開 index.html，即可執行 repo 中的 `script.py`，或直接貼上 raw.githubusercontent.com 的 URL 執行外部 .py 檔案。

快速上手
1. 建立一個新的 GitHub repository（或使用現有的）。
2. 將 `index.html`、`script.py`、以及本 README.md 放到 repo 根目錄（或放到 `docs/` 資料夾）。
3. 到 GitHub → Settings → Pages：選擇分支（例如 `main`）與目錄（`/ (root)` 或 `/docs`），儲存。GitHub 會提供一個像 `https://USERNAME.github.io/REPO/` 的網址。
4. 在 iPhone 的 Safari 開啟該網址。首次載入會下載 Pyodide（數 MB），可能比較慢。
5. 頁面會顯示預設的 Python 程式碼；你可以直接編輯頁面中的程式區塊或填入 raw.githubusercontent.com 的檔案 URL 並按「執行」。

注意與建議
- 若使用 Private Browsing（私密瀏覽），iOS Safari 可能限制 IndexedDB，會造成 Pyodide 無法快取或執行。請用一般瀏覽模式。
- 首次載入 Pyodide 會下載較多資源（幾 MB）；之後會快一些。
- 安全性：在瀏覽器執行 Python 時仍可透過 js 模組呼叫瀏覽器 API，請勿在不信任的程式上執行。
- 如果 fetch raw.githubusercontent.com 遇到 CORS 或其他問題，建議使用同 repo 的 Pages 路徑（同源）。
