/* New Hope Immigration — Exit Popup + Floating CTA + WhatsApp Button
   Loaded on all site pages via <script src="/exit-popup.js" defer></script>
   v2.1 — Jun 2026 */
(function () {
  "use strict";

  /* ── Language detection ── */
  var p = window.location.pathname;
  var lg = p.indexOf("/pt-br/") !== -1 ? "pt" : p.indexOf("/es/") !== -1 ? "es" : "en";

  /* ── Strings ── */
  var T = {
    en: {
      popup_title: "Not sure where to start?",
      popup_body: "Our DOJ-accredited team can review your case in a 45-minute consultation — online or in person in Orlando.",
      popup_cta: "Schedule a $50 Consultation",
      popup_close: "No thanks",
      float_label: "Free Case Review",
      float_title: "Speak with an Accredited Representative",
      float_body: "Get expert guidance on your immigration case. $50 initial consultation — online or in person.",
      float_cta: "Call (407) 275-6163",
      float_alt: "Schedule Online →"
    },
    pt: {
      popup_title: "Não sabe por onde começar?",
      popup_body: "Nossa equipe credenciada pelo DOJ pode avaliar seu caso em uma consulta de 45 minutos — online ou presencial em Orlando.",
      popup_cta: "Agendar Consulta por $50",
      popup_close: "Agora não",
      float_label: "Avaliação Gratuita",
      float_title: "Fale com um Representante Credenciado",
      float_body: "Orientação especializada para o seu caso de imigração. Consulta inicial $50 — online ou presencial.",
      float_cta: "Ligar (407) 275-6163",
      float_alt: "Agendar Online →"
    },
    es: {
      popup_title: "¿No sabe por dónde empezar?",
      popup_body: "Nuestro equipo acreditado por el DOJ puede evaluar su caso en una consulta de 45 minutos — en línea o en persona en Orlando.",
      popup_cta: "Agendar Consulta por $50",
      popup_close: "Ahora no",
      float_label: "Evaluación de Caso",
      float_title: "Hable con un Representante Acreditado",
      float_body: "Orientación para su caso de inmigración. Consulta inicial $50 — en línea o en persona.",
      float_cta: "Llamar (407) 275-6163",
      float_alt: "Agendar en Línea →"
    }
  };
  var s = T[lg];

  /* ── Source tracking ── */
  function src() {
    var r = document.referrer || "";
    if (r.indexOf("google") !== -1) return "google";
    if (r.indexOf("facebook") !== -1 || r.indexOf("instagram") !== -1) return "social";
    if (r.indexOf("nhv-wa-btn") !== -1) return "whatsapp";
    return "direct";
  }

  /* ── Popup markup ── */
  var POPUP_CSS = [
    "#nhv-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:99997;display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .3s}",
    "#nhv-overlay.visible{opacity:1}",
    "#nhv-modal{background:#fff;border-radius:16px;padding:36px 32px 28px;max-width:440px;width:90%;position:relative;transform:translateY(24px);transition:transform .3s;text-align:center;box-shadow:0 24px 80px rgba(0,0,0,.22)}",
    "#nhv-overlay.visible #nhv-modal{transform:translateY(0)}",
    "#nhv-modal-close{position:absolute;top:14px;right:16px;background:none;border:none;font-size:22px;cursor:pointer;color:#94a3b8;line-height:1}",
    "#nhv-modal h2{font-size:22px;font-weight:800;color:#0f172a;margin:0 0 12px;font-family:'Manrope',sans-serif}",
    "#nhv-modal p{font-size:15px;color:#475569;line-height:1.6;margin:0 0 24px;font-family:'Manrope',sans-serif}",
    "#nhv-modal-cta{display:block;background:#469A3D;color:#fff;border:none;border-radius:10px;padding:15px 28px;font-size:16px;font-weight:800;cursor:pointer;text-decoration:none;font-family:'Manrope',sans-serif;transition:background .15s}",
    "#nhv-modal-cta:hover{background:#357a2f}",
    "#nhv-modal-skip{display:block;margin-top:14px;font-size:13px;color:#94a3b8;cursor:pointer;background:none;border:none;font-family:'Manrope',sans-serif}",
    "#nhv-modal-skip:hover{color:#64748b}"
  ].join("");

  /* ── Float panel CSS ── */
  var FLOAT_CSS = [
    "#nhv-float-btn{position:fixed;bottom:24px;right:24px;z-index:99998;width:56px;height:56px;border-radius:50%;background:#469A3D;border:none;cursor:pointer;box-shadow:0 4px 20px rgba(70,154,61,.45);display:flex;align-items:center;justify-content:center;transition:transform .15s,box-shadow .15s}",
    "#nhv-float-btn:hover{transform:scale(1.08);box-shadow:0 6px 28px rgba(70,154,61,.6)}",
    "#nhv-float-panel{position:fixed;bottom:90px;right:24px;z-index:99998;width:300px;background:#fff;border-radius:14px;box-shadow:0 8px 40px rgba(0,0,0,.18);padding:24px 22px 20px;display:none;font-family:'Manrope',sans-serif}",
    "#nhv-float-panel.open{display:block}",
    "#nhv-float-panel h4{font-size:16px;font-weight:800;color:#0f172a;margin:0 0 8px}",
    "#nhv-float-panel p{font-size:13px;color:#475569;line-height:1.55;margin:0 0 16px}",
    "#nhv-float-panel .nhv-fp-cta{display:block;background:#469A3D;color:#fff;text-align:center;padding:12px;border-radius:8px;font-weight:800;font-size:14px;text-decoration:none;margin-bottom:8px}",
    "#nhv-float-panel .nhv-fp-alt{display:block;text-align:center;font-size:13px;color:#469A3D;font-weight:700;text-decoration:none}",
    "#nhv-float-panel .nhv-fp-alt:hover{text-decoration:underline}"
  ].join("");

  /* ── WhatsApp button CSS ── */
  var WA_CSS = [
    "#nhv-wa-btn{position:fixed;bottom:90px;right:24px;z-index:9998;width:52px;height:52px;border-radius:50%;background:#25D366;box-shadow:0 4px 16px rgba(37,211,102,.5);display:flex;align-items:center;justify-content:center;text-decoration:none;transition:transform .15s}",
    "#nhv-wa-btn:hover{transform:scale(1.1)}"
  ].join("");

  /* ── Inject styles ── */
  var style = document.createElement("style");
  style.textContent = POPUP_CSS + FLOAT_CSS + WA_CSS;
  document.head.appendChild(style);

  /* ── Build popup ── */
  var overlay = document.createElement("div");
  overlay.id = "nhv-overlay";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-modal", "true");
  overlay.innerHTML = '<div id="nhv-modal">'
    + '<button id="nhv-modal-close" aria-label="Close">×</button>'
    + '<h2>' + s.popup_title + '</h2>'
    + '<p>' + s.popup_body + '</p>'
    + '<a id="nhv-modal-cta" href="/en/contact-us/?src=exit-popup&ref=' + src() + '">' + s.popup_cta + '</a>'
    + '<button id="nhv-modal-skip">' + s.popup_close + '</button>'
    + '</div>';

  /* ── Build float button + panel ── */
  var floatBtn = document.createElement("button");
  floatBtn.id = "nhv-float-btn";
  floatBtn.setAttribute("aria-label", s.float_label);
  floatBtn.innerHTML = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>';

  var contactHref = lg === "pt" ? "/pt-br/contato/" : lg === "es" ? "/es/contacto/" : "/en/contact-us/";
  var floatPanel = document.createElement("div");
  floatPanel.id = "nhv-float-panel";
  floatPanel.innerHTML = '<h4>' + s.float_title + '</h4>'
    + '<p>' + s.float_body + '</p>'
    + '<a class="nhv-fp-cta" href="tel:+14072756163">' + s.float_cta + '</a>'
    + '<a class="nhv-fp-alt" href="' + contactHref + '?src=float">' + s.float_alt + '</a>';

  /* ── Build WhatsApp button ── */
  var waMsgs = {
    en: "Hi! I found you through newhopevisa.com and I'd like to learn more about my immigration case.",
    pt: "Olá! Encontrei vocês pelo site newhopevisa.com e gostaria de esclarecer dúvidas sobre meu caso de imigração.",
    es: "¡Hola! Los encontré en el sitio web newhopevisa.com y me gustaría resolver dudas sobre mi caso de inmigración."
  };
  var waBtn = document.createElement("a");
  waBtn.id = "nhv-wa-btn";
  waBtn.href = "https://wa.me/14072756163?text=" + encodeURIComponent(waMsgs[lg]);
  waBtn.target = "_blank";
  waBtn.rel = "noopener noreferrer";
  waBtn.setAttribute("aria-label", "WhatsApp");
  waBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="#fff"><path d="M20.52 3.48A11.93 11.93 0 0 0 12 0C5.37 0 0 5.37 0 12c0 2.11.55 4.16 1.6 5.97L0 24l6.18-1.57A11.94 11.94 0 0 0 12 24c6.63 0 12-5.37 12-12 0-3.2-1.25-6.21-3.48-8.52zM12 21.94a9.9 9.9 0 0 1-5.04-1.38l-.36-.21-3.73.95.99-3.62-.24-.37A9.9 9.9 0 0 1 2.06 12C2.06 6.51 6.51 2.06 12 2.06c2.64 0 5.12 1.03 6.99 2.9A9.85 9.85 0 0 1 21.94 12c0 5.49-4.45 9.94-9.94 9.94zm5.47-7.44c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.27-.47-2.42-1.49-.89-.8-1.49-1.78-1.67-2.08-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51-.17 0-.37-.02-.57-.02-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47s1.06 2.86 1.21 3.06c.15.2 2.09 3.18 5.07 4.46.71.3 1.26.48 1.69.62.71.22 1.36.19 1.87.12.57-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35z"/></svg>';

  /* ── DOM ready ── */
  function init() {
    document.body.appendChild(overlay);
    document.body.appendChild(floatBtn);
    document.body.appendChild(floatPanel);
    document.body.appendChild(waBtn);

    /* Float toggle */
    floatBtn.addEventListener("click", function () {
      floatPanel.classList.toggle("open");
    });
    document.addEventListener("click", function (e) {
      if (!floatBtn.contains(e.target) && !floatPanel.contains(e.target)) {
        floatPanel.classList.remove("open");
      }
    });

    /* Popup open/close */
    window.nhvOpenPopup = function (source) {
      overlay.classList.add("visible");
      var cta = document.getElementById("nhv-modal-cta");
      if (cta) cta.href = contactHref + "?src=" + (source || "manual");
    };

    function closePopup() { overlay.classList.remove("visible"); }
    document.getElementById("nhv-modal-close").addEventListener("click", closePopup);
    document.getElementById("nhv-modal-skip").addEventListener("click", closePopup);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) closePopup(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closePopup(); });

    /* Auto-trigger: exit intent (desktop) */
    var triggered = sessionStorage.getItem("nhv-popup-shown");
    if (!triggered) {
      document.addEventListener("mouseleave", function handler(e) {
        if (e.clientY < 5) {
          window.nhvOpenPopup("exit-intent");
          sessionStorage.setItem("nhv-popup-shown", "1");
          document.removeEventListener("mouseleave", handler);
        }
      });
      /* Mobile: scroll up fast */
      var lastY = 0, ticking = false;
      window.addEventListener("scroll", function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
          var y = window.scrollY;
          if (lastY - y > 80 && y > 300 && !sessionStorage.getItem("nhv-popup-shown")) {
            window.nhvOpenPopup("scroll-up");
            sessionStorage.setItem("nhv-popup-shown", "1");
          }
          lastY = y;
          ticking = false;
        });
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
