document.addEventListener("DOMContentLoaded", function() {
    const defaultOptions = {
        buttonColor: '#0048ff',
        buttonIconColor: '#ffffff',
        highlightColor: '#0048ff',
        menuBackgroundColor: '#ffffff',
        menuTextColor: '#333333',
        customLabels: {}
    };

    const userOptions = window.siennaOptions || {};
    const options = { ...defaultOptions, ...userOptions };

    let t = { states: {} };
    const e = function() {
        !function(t, e, s) {
            const a = new Date;
            a.setTime(a.getTime() + 365 * 24 * 60 * 60 * 1000);
            let n = "expires=" + a.toUTCString();
            document.cookie = "asw=" + e + ";" + n + ";path=/"
        }(0, JSON.stringify(t))
    };
    let s = function(t) {
        let e = "asw=", s = decodeURIComponent(document.cookie).split(";");
        for (let t = 0; t < s.length; t++) {
            let a = s[t];
            for (; " " == a.charAt(0);) a = a.substring(1);
            if (0 == a.indexOf(e)) return a.substring(e.length, a.length)
        }
        return ""
    }();
    try {
        s = JSON.parse(s)
    } catch (t) {}
    t = { states: {}, ...s };
    
    let a = ["format_size", "add", "remove", "restart_alt", "close"];
    
    const n = function(e, s) {
        let n = "";
        for (var i = e.length; i--;) {
            let o = e[i], l = t.states[o.key];
            "asw-filter" == s && t.states.contrast == o.key && (l = !0);
            const label = o.label;
            n += `\n<div class="asw-btn ${s || ""} ${l ? "asw-selected" : ""}" role="button" aria-pressed="false" data-key="${o.key}" aria-label="${label}" title="${label}"><span class="material-icons">${o.icon}</span>${label}\n</div>`;
            a.push(o.icon)
        }
        return n
    };
    
    let i = n([
            { label: "Subrayar Enlaces", key: "underline-links", icon: "format_underlined" },
            { label: "Resaltar Título", key: "highlight-title", icon: "title" },
            { label: "Espaciado entre Letras", key: "letter-spacing", icon: "text_increase" },
            { label: "Altura de Línea", key: "line-height", icon: "format_line_spacing" },
            { label: "Grosor de Fuente", key: "font-weight", icon: "format_bold" }
        ]),
        o = n([

            { label: "Alto Contraste", key: "high-contrast", icon: "tonality" },
            { label: "Alta Saturación", key: "high-saturation", icon: "filter_vintage" },
            { label: "Baja Saturación", key: "low-saturation", icon: "gradient" },
            { label: "Monocromo", key: "monochrome", icon: "filter_b_and_w" }
        ], "asw-filter"),
        l = n([
            { label: "Lector de Voz", key: "text-to-speech", icon: "record_voice_over" },
            { label: "Detener Animaciones", key: "stop-animations", icon: "motion_photos_off" },
            { label: "Cursor Grande", key: "big-cursor", icon: "mouse" }
        ], "asw-tools");
    
    var r = document.createElement("div");
    r.innerHTML = `
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons&text=${a.toString()}" rel="stylesheet">
    <style>
        :root {
           --asw-bg-light: #ffffff;
            --asw-text-light: #333333;
            --asw-card-light: #ecf3ff;
            --asw-header-light: #161719;
            --asw-bg-dark: #0f0f23;
            --asw-text-dark: #e0e0e0;
            --asw-card-dark: #1a1a2e;
            --asw-header-dark: #0f3460;
            --asw-border-dark: #161719;
        }

        .asw-menu, .asw-menu-btn { position: fixed; left: 2px; transition: .3s; z-index: 400000;}
        .asw-widget { -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; font-weight: 400; -webkit-font-smoothing: antialiased; }
        .asw-widget * { box-sizing: border-box; }
        .asw-menu-btn { bottom: 20px; background: ${options.buttonColor}; box-shadow: 0 5px 15px 0 rgb(37 44 97 / 15%), 0 2px 4px 0 rgb(93 100 148 / 20%); border-radius: 50%; align-items: center; justify-content: center; transform: translateY(0); width: 50px; height: 50px; display: flex; fill: ${options.buttonIconColor} !important; cursor: pointer; }
        .asw-menu-btn svg { width: 30px; height: 30px; min-height: 30px; min-width: 30px; max-width: 30px; max-height: 30px; background: 0 0 !important; }
        .asw-menu-btn:hover { transform: scale(1.05); }
        .asw-menu { display: none; top: 20px; border-radius: 8px; box-shadow: -1px 0 20px -14px #000; opacity: 1; overflow: hidden; background: var(--asw-bg-light); width: 500px; line-height: 1; font-size: 14px; height: calc(100vh - 40px - 75px); letter-spacing: .015em; color: var(--asw-text-light); }
        .asw-btn, .asw-footer a { font-size: 14px !important; }
        .asw-menu-header { display: flex; align-items: center; justify-content: space-between; background: #0334b1; color: #fff; padding-left: 12px; font-weight: 600; }
        .asw-menu-header > div { display: flex; }
        .asw-menu-header div[role=button] { padding: 12px; cursor: pointer; }
        .asw-menu-header div[role=button]:hover, .asw-minus:hover, .asw-plus:hover { opacity: .8; }
        .asw-items { display: flex; gap: 10px; padding: 0; list-style: none; flex-wrap: wrap; justify-content: space-between; }
        .asw-btn { width: 140px; height: 120px; border-radius: 8px; padding: 15px; display: flex; align-items: center; justify-content: center; flex-direction: column; text-align: center; color: #333; background: #ecf3ff; border: 3px solid #ecf3ff; transition: background-color .3s; cursor: pointer; }
        .asw-btn .material-icons { margin-bottom: 16px; }
        .asw-btn:hover { border-color: ${options.highlightColor}; }
        .asw-btn.asw-selected { background: ${options.highlightColor}; color: #fff; border-color: ${options.highlightColor}; }
        .asw-footer { position: absolute; bottom: 0; left: 0; right: 0; background: #0334b1; padding: 16px; text-align: center; color: #fff; }
        .asw-footer a { text-decoration: underline; color: #fff; background: 0 0 !important; }
        .asw-menu-content { overflow: scroll; max-height: calc(100% - 80px); }
        .asw-card { margin: 0 15px 30px; }
        .asw-card-title { font-size: 18px; padding: 15px 0; }
        .asw-adjust-font { background: #ecf3ff; padding: 20px 25px; margin-bottom: 16px; border-radius: 8px; }
        .asw-adjust-font .label { display: flex; align-items: center; }
        .asw-adjust-font > div { display: flex; justify-content: space-between; margin-top: 20px; align-items: center; font-size: 16px; font-weight: 700; }
        .asw-adjust-font div[role=button] { background: #0648ff; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; color: #fff; cursor: pointer; }
        .asw-reset-btn { background: #0048ff; color: white; border: none; border-radius: 8px; padding: 15px 30px; width: calc(100% - 30px); margin: 0 15px 20px; cursor: pointer; font-size: 16px; font-weight: 600; transition: .3s; }
        .asw-reset-btn:hover { background: #0038cc; }
        .asw-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 10000; display: none; }

        /* Estilos para Lector de Voz */
        .asw-tts-notification {
            position: fixed;
            bottom: 90px;
            left: 20px;
            background: #0048ff;
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            z-index: 500001;
            display: none;
            align-items: center;
            gap: 12px;
            font-size: 14px;
            max-width: 300px;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from {
                transform: translateX(-100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }

        .asw-tts-notification.show {
            display: flex;
        }

        .asw-tts-controls {
            display: flex;
            gap: 8px;
        }

        .asw-tts-btn {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
        }

        .asw-tts-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.1);
        }

        .asw-tts-btn .material-icons {
            font-size: 18px;
        }

        body.text-to-speech-active {
            cursor: help !important;
        }



        @media only screen and (max-width: 560px) {
            .asw-menu { width: calc(100vw - 20px); left: 10px; }
            .asw-btn { width: calc(50% - 8px); }
            .asw-tts-notification {
                left: 10px;
                right: 10px;
                max-width: calc(100vw - 20px);
                bottom: 80px;
            }
        }
    </style>
    <div class="asw-widget">
        <div class="asw-menu-btn" title="Abrir Menú de Accesibilidad" role="button" aria-expanded="false">
            <svg xmlns="http://www.w3.org/2000/svg" style="width:34px;height:34px;min-height:34px;min-width:34px;max-width:34px;max-height:34px;" viewBox="0 0 24 24" width="34px" height="34px">
                <path d="M0 0h24v24H0V0z" fill="none"/>
                <path d="M20.5 6c-2.61.7-5.67 1-8.5 1s-5.89-.3-8.5-1L3 8c1.86.5 4 .83 6 1v13h2v-6h2v6h2V9c2-.17 4.14-.5 6-1l-.5-2zM12 6c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z"/>
            </svg>
        </div>
        <div class="asw-menu">
            <div class="asw-menu-header">Menú de Accesibilidad
                <div>
                    <div role="button" class="asw-menu-close" title="Cerrar Menú">
                        <span class="material-icons">close</span>
                    </div>
                </div>
            </div>
            <div class="asw-menu-content">
                <div class="asw-card" style="margin-top: 15px;">
                    <div class="asw-card-title">Ajustes</div>
                    <div class="asw-adjust-font">
                        <div class="label">
                            <span class="material-icons" style="margin-right:8px;">format_size</span> Tamaño de Fuente
                        </div>
                        <div>
                            <div class="asw-minus" data-key="font-size" role="button" aria-pressed="false">
                                <span class="material-icons">remove</span>
                            </div>
                            <div class="asw-amount">${t.states.fontSize && 1 != t.states.fontSize ? `${parseInt(100 * t.states.fontSize)}%` : "Normal"}</div>
                            <div class="asw-plus" data-key="font-size" role="button" aria-pressed="false">
                                <span class="material-icons">add</span>
                            </div>
                        </div>
                    </div>
                    <div class="asw-items">${i}</div>
                </div>
                <div class="asw-card" style="margin-top: 15px;">
                    <div class="asw-card-title">Ajustes de Color</div>
                    <div class="asw-items">${o}</div>
                </div>
                <div class="asw-card" style="margin-top: 15px;">
                    <div class="asw-card-title">Herramientas</div>
                    <div class="asw-items">${l}</div>
                </div>
                <button class="asw-reset-btn">Restablecer Configuración</button>
            </div>
            <div class="asw-footer">
                <a>Suazapawa Accesibilidad</a>
            </div>
        </div>
        <div class="asw-overlay"></div>
        <div class="asw-tts-notification">
            <span class="material-icons">record_voice_over</span>
            <span class="asw-tts-text">Pasa el cursor sobre el texto</span>
            <div class="asw-tts-controls">
                <button class="asw-tts-btn asw-tts-stop" title="Detener">
                    <span class="material-icons">stop</span>
                </button>
            </div>
        </div>
    </div>`;

    // Sistema de Text-to-Speech
    let speechSynth = window.speechSynthesis;
    let currentUtterance = null;
    let ttsNotification = null;
    let lastSpokenText = '';
    let hoverTimeout = null;
    let isReady = false;

    const initTTS = function() {
        ttsNotification = document.querySelector('.asw-tts-notification');
        const stopBtn = document.querySelector('.asw-tts-stop');

        if (stopBtn) {
            stopBtn.addEventListener('click', function() {
                if (speechSynth.speaking) {
                    speechSynth.cancel();
                }
            });
        }

        if (speechSynth.onvoiceschanged !== undefined) {
            speechSynth.onvoiceschanged = () => {
                isReady = true;
            };
        }

        setTimeout(() => {
            isReady = true;
        }, 100);

        attachHoverListeners();
    };

    const attachHoverListeners = function() {
        const textElements = 'p, h1, h2, h3, h4, h5, h6, span, a, li, td, th, label, button, div, section, article, header, footer, nav, main, strong, em, small, code';

        document.addEventListener('mouseover', function(event) {
            if (!t.states['text-to-speech']) return;

            const target = event.target;
            if (target.closest('.asw-widget')) return;
            if (target.classList.contains('material-icons')) return;

            if (target.matches(textElements)) {
                clearTimeout(hoverTimeout);
                hoverTimeout = setTimeout(() => {
                    let text = '';

                    let childText = Array.from(target.childNodes)
                        .filter(node => node.nodeType === Node.TEXT_NODE)
                        .map(node => node.textContent.trim())
                        .filter(txt => txt.length > 0)
                        .join(' ');

                    if (childText) {
                        text = childText;
                    } else {
                        text = target.textContent.trim();
                    }

                    const isValidElement = text &&
                        text.length > 0 &&
                        text.length < 500 &&
                        !target.classList.contains('material-icons') &&
                        !target.classList.contains('asw-widget') &&
                        !target.closest('script') &&
                        !target.closest('style') &&
                        !target.closest('.asw-widget');

                    if (isValidElement) {
                        speakText(text);
                    }
                }, 300);
            }
        });

        document.addEventListener('mouseout', function(event) {
            if (!t.states['text-to-speech']) return;
            clearTimeout(hoverTimeout);
        });
    };

    const speakText = function(text) {
        if (!isReady) return;
        if (text === lastSpokenText && speechSynth.speaking) return;

        if (speechSynth.speaking) {
            speechSynth.cancel();
        }

        lastSpokenText = text;

        if (text.length > 300) {
            text = text.substring(0, 300);
        }

        currentUtterance = new SpeechSynthesisUtterance(text);

        const voices = speechSynth.getVoices();
        const spanishVoice = voices.find(voice => voice.lang.startsWith('es'));
        if (spanishVoice) {
            currentUtterance.voice = spanishVoice;
        }

        currentUtterance.lang = 'es-ES';
        currentUtterance.rate = 1.1;
        currentUtterance.pitch = 1.0;
        currentUtterance.volume = 1.0;

        const ttsText = ttsNotification.querySelector('.asw-tts-text');
        ttsText.textContent = 'Leyendo...';
        ttsNotification.classList.add('show');

        currentUtterance.onend = function() {
            ttsText.textContent = 'Pasa el cursor sobre el texto';
            setTimeout(() => {
                if (!speechSynth.speaking) {
                    ttsNotification.classList.remove('show');
                }
            }, 1500);
            lastSpokenText = '';
        };

        currentUtterance.onerror = function(event) {
            console.log('TTS Error:', event);
            lastSpokenText = '';
        };

        try {
            speechSynth.speak(currentUtterance);
        } catch (error) {
            console.log('TTS Error:', error);
        }
    };

    const c = function(t, e) {
        let s = document.getElementById(e || "") || document.createElement("style");
        s.innerHTML = t, s.id || (s.id = e, document.head.appendChild(s))
    }, d = function(t, e) {
        let s = "", a = ["-o-", "-ms-", "-moz-", "-webkit", ""];
        for (var n = a.length; n--;) s += a[n] + (e || "filter") + ":" + t + ";";
        return s
    }, p = function(t) {
        let e = "";
        if (t) {
            let a = "";
            "dark-contrast" == t ? a = "color: #fff !important;fill: #FFF !important;background-color: #000 !important;" : "light-contrast" == t ? a = "color: #000 !important;fill: #000 !important;background-color: #FFF !important;" : "high-contrast" == t ? a += d("contrast(125%)") : "high-saturation" == t ? a += d("saturate(200%)") : "low-saturation" == t ? a += d("saturate(50%)") : "monochrome" == t && (a += d("grayscale(100%)"));
            let n = [""];
            "dark-contrast" != t && "light-contrast" != t || (n = ["h1", "h2", "h3", "h4", "h5", "h6", "img", "p", "i", "svg", "a", "button", "label", "li", "ol"]);
            for (var s = n.length; s--;) e += '[data-asw-filter="' + t + '"] ' + n[s] + "{" + a + "}"
        }
        c(e, "asw-filter-style"), t ? document.documentElement.setAttribute("data-asw-filter", t) : document.documentElement.removeAttribute("data-asw-filter", t)
    }, u = function() {
        let e = [{
            id: "highlight-title",
            childrenSelector: ["h1", "h2", "h3", "h4", "h5", "h6"],
            css: "outline: 2px solid " + options.highlightColor + " !important;outline-offset: 2px !important;"
        }, {
            id: "readable-font",
            childrenSelector: ["", "h1", "h2", "h3", "h4", "h5", "h6", "img", "p", "i", "svg", "a", "button", "label", "li", "ol"],
            css: "font-family: OpenDyslexic3,Comic Sans MS,Arial,Helvetica,sans-serif !important;"
        }, {
            id: "letter-spacing",
            childrenSelector: ["p", "span", "a", "li", "td", "th"],
            css: "letter-spacing: 0.12em !important;"
        }, {
            id: "line-height",
            childrenSelector: ["p", "span", "a", "li", "td", "th"],
            css: "line-height: 2 !important;"
        }, {
            id: "font-weight",
            childrenSelector: ["p", "span", "a", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6"],
            css: "font-weight: 700 !important;"
        }, {
            id: "underline-links",
            childrenSelector: ["a[href]"],
            css: "text-decoration: underline !important; text-decoration-thickness: 2px !important; text-underline-offset: 4px !important;"
        }], s = "";
        for (var a = e.length; a--;) {
            let i = e[a];
            if (document.documentElement.classList.toggle(i.id, !!t.states[i.id]), t.states[i.id]) for (var n = i.childrenSelector.length; n--;) s += "." + i.id + " " + i.childrenSelector[n] + "{" + i.css + "}"
        }

        if (t.states['text-to-speech']) {
            document.body.classList.add('text-to-speech-active');
            if (ttsNotification) {
                ttsNotification.classList.add('show');
            }
        } else {
            document.body.classList.remove('text-to-speech-active');
            if (ttsNotification) {
                ttsNotification.classList.remove('show');
            }
            if (speechSynth.speaking) {
                speechSynth.cancel();
            }
            clearTimeout(hoverTimeout);
        }

        var i = document.querySelector(".asw-rg-container");
        if (false) {
        } else if (i) {
            i.remove();
        }
        t.states["stop-animations"] && (s += `\nbody * {${d("none !important", "transition")}${d("forwards !important", "animation-fill-mode")}${d("1 !important", "animation-iteration-count")}${d(".01s !important", "animation-duration")}\n}`), t.states["big-cursor"] && (s += "\nbody * {cursor: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='64' height='64' viewBox='0 0 512 512'%3E%3Cpath d='M429.742 319.31L82.49 0l-.231 471.744 105.375-100.826 61.89 141.083 96.559-42.358-61.89-141.083 145.549-9.25zM306.563 454.222l-41.62 18.259-67.066-152.879-85.589 81.894.164-333.193 245.264 225.529-118.219 7.512 67.066 152.878z' xmlns='http://www.w3.org/2000/svg'/%3E%3C/svg%3E\") ,default !important;\n}"), t.states["readable-font"] && (s += '\n@font-face {font-family: OpenDyslexic3;src: url("https://website-widgets.pages.dev/fonts/OpenDyslexic3-Regular.woff") format("woff"), url("https://website-widgets.pages.dev/fonts/OpenDyslexic3-Regular.ttf") format("truetype");\n}'), c(s, "asw-content-style")
    };

    var f = function(s) {
        s.preventDefault();
        let a = s.currentTarget, n = a.dataset.key;
        a.classList.contains("asw-filter") ? (document.querySelectorAll(".asw-filter").forEach((function(t) {
            t.classList.remove("asw-selected"), t.setAttribute("aria-pressed", "false")
        })), t.states.contrast = t.states.contrast !== n && n, t.states.contrast && (a.classList.add("asw-selected"), a.setAttribute("aria-pressed", "true")), p(t.states.contrast)) : (t.states[n] = !t.states[n], a.classList.toggle("asw-selected", t.states[n]), a.setAttribute("aria-pressed", t.states[n] ? "true" : "false"), u()), e()
    };

    const h = function(e, s) {
        let a = !1;
        !s && e && (a = e.currentTarget, s = parseFloat(t.states.fontSize) || 1, a.classList.contains("asw-minus") ? s -= .1 : s += .1, s = Math.max(s, .1), s = Math.min(s, 2), s = parseFloat(s.toFixed(2))), document.querySelectorAll("h1,h2,h3,h4,h5,h6,p,a,dl,dt,li,ol,th,td,span").forEach((function(t) {
            if (!t.classList.contains("material-icons")) {
                let e = t.getAttribute("data-asw-orgFontSize");
                e || (e = parseInt(window.getComputedStyle(t, null).getPropertyValue("font-size")), t.setAttribute("data-asw-orgFontSize", e));
                let a = e * s;
                t.style["font-size"] = a + "px"
            }
        }));
        let n = "Normal";
        1 !== s && (n = `${parseInt(100 * s)}%`), a && (a.parentElement.querySelector(".asw-amount").innerHTML = n), t.states.fontSize = s
    };

    let m = r.querySelector(".asw-menu"),
        g = r.querySelector(".asw-overlay");
    r.querySelector(".asw-menu-btn").addEventListener("click", function() {
        let isVisible = m.style.display === "block";
        m.style.display = isVisible ? "none" : "block";
        g.style.display = m.style.display;
    }, false);
    m.querySelector(".asw-menu-close").addEventListener("click", function() {
        m.style.display = "none";
        g.style.display = m.style.display;
    }, false);
    g.addEventListener("click", function() {
        m.style.display = "none";
        g.style.display = "none";
    }, false);

    m.querySelector(".asw-reset-btn").addEventListener("click", function() {
        t.states = {};
        p(), u(), h(void 0, 1), document.querySelectorAll(".asw-btn").forEach(function(t) {
            t.classList.remove("asw-selected"), t.setAttribute("aria-pressed", "false")
        }), document.querySelectorAll(".asw-amount").forEach(function(t) {
            t.innerHTML = "Normal"
        }), e()
    }, false);

    m.querySelectorAll(".asw-btn").forEach(function(t) {
        t.addEventListener("click", f, false)
    });
    m.querySelectorAll(".asw-adjust-font div[role='button']").forEach(function(t) {
        t.addEventListener("click", function(t) {
            h(t), e()
        }, false)
    });
    document.body.appendChild(r);

    initTTS();
    
    if (s) {
        u();
        if (1 !== t.states.fontSize) h(null, t.states.fontSize);
        if (t.states.contrast) p(t.states.contrast);
    }
});