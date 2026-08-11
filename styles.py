EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026"
]

HEADER_HTML = """
<div class="dr-brand">
    <div class="dr-brand-icon">
        <div class="dr-glow-orb"></div>
        <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            <path d="M11 8v6M8 11h6"></path>
        </svg>
    </div>
    <div class="dr-titles">
        <h1>Deep<span class="dr-gradient-text">/Research</span></h1>
        <p><span class="dr-badge">AI AGENT ENGINE</span> Multi-Search Autonomous Investigation</p>
    </div>
</div>
"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --dr-font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --dr-font-heading: 'Outfit', sans-serif;
    --dr-font-mono: 'JetBrains Mono', monospace;

    --dr-bg-gradient: radial-gradient(circle at 50% 0%, #171e36 0%, #0b0f19 75%);
    --dr-surface-glass: rgba(19, 27, 46, 0.75);
    --dr-surface-card: #111827;
    --dr-surface-hover: #1c2845;
    --dr-border: rgba(255, 255, 255, 0.1);
    --dr-border-glow: rgba(99, 102, 241, 0.4);
    
    --dr-text-primary: #f8fafc;
    --dr-text-secondary: #cbd5e1;
    --dr-text-muted: #64748b;

    --dr-indigo: #6366f1;
    --dr-purple: #8b5cf6;
    --dr-cyan: #06b6d4;
    --dr-emerald: #10b981;

    --dr-gradient-primary: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%);
    --dr-gradient-accent: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);
}

html, body, gradio-app, #root, .gradio-container-wrapper {
    background-color: #0b0f19 !important;
    background: var(--dr-bg-gradient) !important;
    color: var(--dr-text-primary) !important;
    font-family: var(--dr-font-main) !important;
    margin: 0 !important;
    padding: 0 !important;
    min-height: 100vh !important;
    width: 100% !important;
}

.gradio-container {
    max-width: 1060px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2rem 4rem !important;
    background: transparent !important;
    min-height: 100vh !important;
    font-family: var(--dr-font-main) !important;
}

/* === HEADER BRAND === */
.dr-brand {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    padding-bottom: 1.5rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid var(--dr-border);
    position: relative;
}

.dr-brand-icon {
    position: relative;
    width: 52px;
    height: 52px;
    border-radius: 16px;
    background: var(--dr-gradient-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    box-shadow: 0 0 25px rgba(99, 102, 241, 0.4);
}

.dr-glow-orb {
    position: absolute;
    inset: -4px;
    border-radius: 20px;
    background: var(--dr-gradient-primary);
    filter: blur(12px);
    opacity: 0.5;
    z-index: -1;
}

.dr-titles h1 {
    font-family: var(--dr-font-heading);
    font-size: clamp(2rem, 4.5vw, 2.75rem);
    font-weight: 800;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1.05;
    color: #ffffff;
}

.dr-gradient-text {
    color: #c084fc !important;
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%) !important;
    background-clip: text !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    display: inline-block !important;
}

.dr-titles p {
    font-size: 0.85rem;
    color: var(--dr-text-secondary);
    margin: 0.4rem 0 0;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-weight: 500;
}

.dr-badge {
    font-family: var(--dr-font-mono);
    font-size: 0.65rem;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    background: rgba(99, 102, 241, 0.15);
    color: #a5b4fc;
    border: 1px solid rgba(99, 102, 241, 0.3);
    font-weight: 600;
    letter-spacing: 0.05em;
}

/* === SEARCH / QUERY ROW === */
.dr-query-row {
    gap: 0.75rem !important;
    align-items: stretch !important;
    background: var(--dr-surface-glass) !important;
    backdrop-filter: blur(16px) !important;
    padding: 0.6rem !important;
    border-radius: 18px !important;
    border: 1px solid var(--dr-border) !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
    transition: all 0.25s ease !important;
}

.dr-query-row:focus-within {
    border-color: var(--dr-border-glow) !important;
    box-shadow: 0 20px 45px rgba(99, 102, 241, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: transparent !important;
    color: #ffffff !important;
    border: none !important;
    padding: 0.85rem 1.1rem !important;
    font-size: 1.05rem !important;
    font-family: var(--dr-font-main) !important;
    font-weight: 500 !important;
    line-height: 1.5 !important;
    resize: none !important;
    min-height: 52px !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    box-shadow: none !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-text-muted) !important;
}

#dr-run {
    background: var(--dr-gradient-primary) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: var(--dr-font-heading) !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    font-size: 0.9rem !important;
    padding: 0.85rem 1.75rem !important;
    cursor: pointer !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    min-width: 145px !important;
}

#dr-run:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.5) !important;
    filter: brightness(1.1) !important;
}

#dr-run:active {
    transform: translateY(0) !important;
}

/* === EXAMPLES CHIPS === */
.dr-examples-label {
    font-family: var(--dr-font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    color: var(--dr-text-muted);
    text-transform: uppercase;
    margin: 1.25rem 0 0.5rem 0;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-border);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    margin-bottom: 0.5rem !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: 100% !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }
#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: var(--dr-surface-glass) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid var(--dr-border) !important;
    padding: 0.6rem 1.1rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    font-size: 0.88rem !important;
    color: var(--dr-text-secondary) !important;
    border-radius: 12px !important;
    margin: 0 !important;
    text-align: left !important;
    font-weight: 500 !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
}

#dr-examples td:hover, #dr-examples button:hover {
    border-color: var(--dr-indigo) !important;
    color: #ffffff !important;
    background: var(--dr-surface-hover) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(99, 102, 241, 0.25) !important;
}

/* === GLOWING LIVE STATUS CARD === */
.dr-status-box {
    display: flex;
    align-items: center;
    gap: 1.1rem;
    padding: 1.1rem 1.4rem;
    background: rgba(17, 24, 39, 0.95);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(99, 102, 241, 0.4);
    border-radius: 16px;
    margin: 1rem 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    animation: statusGlow 2.5s infinite ease-in-out;
}

@keyframes statusGlow {
    0%, 100% { border-color: rgba(99, 102, 241, 0.4); box-shadow: 0 0 15px rgba(99, 102, 241, 0.25); }
    50% { border-color: rgba(217, 70, 239, 0.7); box-shadow: 0 0 25px rgba(217, 70, 239, 0.4); }
}

.dr-status-spinner {
    width: 26px;
    height: 26px;
    border: 3px solid rgba(165, 180, 252, 0.2);
    border-top-color: #c084fc;
    border-radius: 50%;
    animation: spin 0.85s linear infinite;
    flex-shrink: 0;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.dr-status-info {
    flex: 1;
}

.dr-status-title {
    font-family: var(--dr-font-heading);
    font-size: 1.05rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0;
}

.dr-status-sub {
    font-size: 0.82rem;
    color: #a5b4fc;
    margin: 0.2rem 0 0 0;
    font-weight: 500;
}

/* === CLARIFICATION CARD === */
#dr-clarification-box {
    margin-top: 1rem !important;
    margin-bottom: 0.5rem !important;
    padding: 1.5rem !important;
    background: #111827 !important;
    border: 1px solid rgba(99, 102, 241, 0.4) !important;
    border-radius: 16px !important;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
}

#dr-clarification-box[style*="display: none"],
.dr-clarification-box[style*="display: none"],
.dr-clarification-box.hidden,
div:has(> #dr-clarification-box[style*="display: none"]) {
    margin: 0 !important;
    padding: 0 !important;
    height: 0 !important;
    min-height: 0 !important;
    border: none !important;
    display: none !important;
}

#dr-clarification, #dr-clarification * {
    color: #f1f5f9 !important;
}

#dr-clarification h3 {
    color: #a5b4fc !important;
    font-family: var(--dr-font-heading) !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    margin-top: 0 !important;
    margin-bottom: 1rem !important;
}

#dr-clarification ol, #dr-clarification ul {
    padding-left: 1.25rem !important;
    margin: 0.75rem 0 !important;
}

#dr-clarification li {
    color: #f1f5f9 !important;
    font-size: 0.98rem !important;
    line-height: 1.6 !important;
    margin-bottom: 0.6rem !important;
}

#dr-clarification strong {
    color: #ffffff !important;
    font-weight: 700 !important;
}

#dr-clarification p, #dr-clarification em {
    color: #cbd5e1 !important;
    font-size: 0.92rem !important;
}

/* === ANSWERS TEXTBOX (CLEAN DARK GLASS INTEGRATION - NO WHITE BOX) === */
#dr-answers, 
#dr-answers *, 
#dr-answers > div, 
#dr-answers .wrap, 
#dr-answers .form, 
#dr-answers fieldset, 
#dr-answers .block,
#dr-answers .container,
#dr-answers div[data-testid="textbox"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

#dr-answers label, #dr-answers span {
    color: #a5b4fc !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    margin-bottom: 0.5rem !important;
    margin-top: 0.75rem !important;
    display: block !important;
    background: transparent !important;
}

#dr-answers textarea {
    background: #0f172a !important;
    color: #ffffff !important;
    border: 1px solid rgba(99, 102, 241, 0.4) !important;
    border-radius: 12px !important;
    padding: 0.85rem 1rem !important;
    font-family: var(--dr-font-main) !important;
    font-size: 0.95rem !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.2s ease !important;
}

#dr-answers textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 15px rgba(99, 102, 241, 0.4), inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    outline: none !important;
}

#dr-answers textarea::placeholder {
    color: #64748b !important;
}

#dr-continue {
    margin-top: 1rem !important;
    background: var(--dr-gradient-primary) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: var(--dr-font-heading) !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
    padding: 0.85rem 1.5rem !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35) !important;
    transition: all 0.2s ease !important;
}

#dr-continue:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.45) !important;
}

#dr-skip {
    margin-top: 1rem !important;
    background: rgba(255, 255, 255, 0.05) !important;
    color: #cbd5e1 !important;
    border: 1px solid var(--dr-border) !important;
    border-radius: 12px !important;
    font-family: var(--dr-font-heading) !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    padding: 0.85rem 1.5rem !important;
    transition: all 0.2s ease !important;
}

#dr-skip:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
}

/* === REPORT & ALL MARKDOWN CONTENT === */
#dr-report {
    margin-top: 0.5rem !important;
    margin-bottom: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    color: #f1f5f9 !important;
    min-height: 0 !important;
}

#dr-report > div, #dr-report .prose {
    background: transparent !important;
    color: #f1f5f9 !important;
}

#dr-report p, #dr-report div, #dr-report span {
    color: #cbd5e1 !important;
    line-height: 1.75 !important;
    font-size: 1rem !important;
}

#dr-report strong, #dr-report b {
    color: #f8fafc !important;
    font-weight: 700 !important;
}

#dr-report em, #dr-report i {
    color: #a5b4fc !important;
}

#dr-report h1 {
    font-family: var(--dr-font-heading);
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    background: var(--dr-gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
    padding-bottom: 0.5rem !important;
    margin: 0.75rem 0 1rem !important;
}

#dr-report h2 {
    font-family: var(--dr-font-heading);
    font-size: 1.4rem !important;
    color: #c084fc !important;
    font-weight: 700 !important;
    margin-top: 1.25rem !important;
    margin-bottom: 0.75rem !important;
}

#dr-report h3, #dr-report h4, #dr-report h5, #dr-report h6 {
    font-family: var(--dr-font-heading) !important;
    font-size: 1.15rem !important;
    color: #38bdf8 !important;
    font-weight: 700 !important;
    margin-top: 1.1rem !important;
    margin-bottom: 0.5rem !important;
}

#dr-report ul, #dr-report ol {
    padding-left: 1.5rem !important;
    margin: 0.75rem 0 !important;
}

#dr-report li {
    color: #cbd5e1 !important;
    margin: 0.4rem 0 !important;
    line-height: 1.7 !important;
}

#dr-report li strong {
    color: #f8fafc !important;
}

#dr-report table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: 100% !important;
    margin: 1.25rem 0 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    background: #0f172a !important;
}

#dr-report th {
    background: #1e293b !important;
    font-weight: 700 !important;
    color: #a5b4fc !important;
    font-family: var(--dr-font-heading) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
    padding: 0.8rem 1rem !important;
    text-align: left !important;
}

#dr-report td {
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding: 0.75rem 1rem !important;
    color: #e2e8f0 !important;
    background: #0f172a !important;
}

#dr-report td strong {
    color: #ffffff !important;
}

#dr-report tr:last-child td {
    border-bottom: none !important;
}

#dr-report tr:hover td {
    background: #1e293b !important;
}

footer { display: none !important; }

@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-query-row { flex-direction: column !important; }
    #dr-run { width: 100% !important; }
}
"""

JS = """
() => {
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    focus();

    // Auto-scroll observer when status or report updates
    const observer = new MutationObserver(() => {
        const reportEl = document.querySelector("#dr-report, #dr-clarification-box");
        if (reportEl && reportEl.textContent.trim().length > 0) {
            const rect = reportEl.getBoundingClientRect();
            if (rect.top > window.innerHeight - 80 || rect.top < 0) {
                reportEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        }
    });

    const target = document.body;
    observer.observe(target, { childList: true, subtree: true, characterData: true });
}
"""
