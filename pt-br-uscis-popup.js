(function () {
	"use strict";

	var STORAGE_KEY = "newhope-uscis-memo-2026-05-v2";

	if (localStorage.getItem(STORAGE_KEY) === "1") {
		return;
	}

	var overlay = document.createElement("div");
	overlay.className = "nhv-popup-overlay";
	overlay.id = "nhv-uscis-popup";
	overlay.setAttribute("role", "dialog");
	overlay.setAttribute("aria-modal", "true");
	overlay.setAttribute("aria-labelledby", "nhv-uscis-popup-title");
	overlay.innerHTML =
		'<div class="nhv-popup">' +
		'<button type="button" class="nhv-popup__close" aria-label="Fechar aviso">&times;</button>' +
		'<div class="nhv-popup__header">' +
		'<h2 class="nhv-popup__title" id="nhv-uscis-popup-title">Memorando USCIS — Ajuste de Status</h2>' +
		'<p class="nhv-popup__subtitle">Publicado em 22 de maio de 2026</p>' +
		"</div>" +
		'<div class="nhv-popup__body">' +
		'<p class="nhv-popup__greeting">Boa tarde,</p>' +
		"<p>Gostaríamos de compartilhar alguns esclarecimentos sobre o memorando publicado pela USCIS em 22 de maio de 2026, referente aos processos de Ajuste de Status.</p>" +
		"<p>O memorando reforça que, de acordo com a Seção 245 do INA (Immigration and Nationality Act), o Ajuste de Status é considerado um benefício discricionário e extraordinário. Isso significa que, mesmo quando o estrangeiro preenche os requisitos básicos de elegibilidade, a aprovação do caso não é automática. A decisão final depende da análise e da discricionariedade do oficial responsável pelo processo.</p>" +
		"<p>Segundo a USCIS, sempre existiu o entendimento de que nem todos os aplicantes elegíveis terão o Ajuste de Status aprovado. O oficial poderá analisar as evidências apresentadas, o histórico imigratório e outros fatores relevantes para determinar se a concessão do benefício é apropriada e de interesse dos Estados Unidos.</p>" +
		"<p>O memorando também destaca que o Ajuste de Status não foi criado para substituir o processo consular regular, mas sim para situações específicas previstas pela lei.</p>" +
		"<p>Dessa forma, após a entrevista e análise do caso, o aplicante poderá receber a aprovação do Ajuste de Status ou ser direcionado ao processamento consular. Isso não significa necessariamente que a pessoa perderá a possibilidade de legalização, porém o processo poderá se tornar mais longo e gerar custos adicionais.</p>" +
		"<p>Na análise discricionária, a USCIS orienta os oficiais a considerarem a totalidade das circunstâncias do caso, incluindo fatores positivos e negativos. Entre os pontos que podem ser analisados estão:</p>" +
		"<ul>" +
		"<li>violações imigratórias ou de status;</li>" +
		"<li>trabalho sem autorização;</li>" +
		"<li>fraude ou falsas informações;</li>" +
		"<li>histórico imigratório;</li>" +
		"<li>laços familiares;</li>" +
		"<li>caráter moral;</li>" +
		"<li>fatores humanitários e outras evidências favoráveis.</li>" +
		"</ul>" +
		"<p>Embora, em teoria, essas diretrizes sempre tenham se aplicado aos processos de Ajuste de Status, ainda não sabemos exatamente como este novo memorando afetará os casos atualmente em andamento. No entanto, entendemos que as análises poderão se tornar mais criteriosas e rigorosas.</p>" +
		"<p>Continuaremos acompanhando as orientações da USCIS e manteremos nossos clientes informados sobre quaisquer mudanças relevantes.</p>" +
		'<p class="nhv-popup__signature">Atenciosamente,<br>New Hope Immigration</p>' +
		"</div>" +
		'<div class="nhv-popup__footer">' +
		'<label class="nhv-popup__dismiss-label">' +
		'<input type="checkbox" id="nhv-uscis-popup-hide" />' +
		"Não exibir novamente" +
		"</label>" +
		'<button type="button" class="nhv-popup__btn" id="nhv-uscis-popup-ok">Entendi</button>' +
		"</div>" +
		"</div>";

	document.body.appendChild(overlay);

	var closeBtn = overlay.querySelector(".nhv-popup__close");
	var okBtn = overlay.querySelector("#nhv-uscis-popup-ok");
	var hideCheckbox = overlay.querySelector("#nhv-uscis-popup-hide");
	var lastFocus = null;

	function openPopup() {
		lastFocus = document.activeElement;
		overlay.classList.add("is-open");
		document.body.classList.add("nhv-popup-open");
		closeBtn.focus();
	}

	function closePopup() {
		if (hideCheckbox.checked) {
			localStorage.setItem(STORAGE_KEY, "1");
		}
		overlay.classList.remove("is-open");
		document.body.classList.remove("nhv-popup-open");
		if (lastFocus && typeof lastFocus.focus === "function") {
			lastFocus.focus();
		}
	}

	closeBtn.addEventListener("click", closePopup);
	okBtn.addEventListener("click", closePopup);

	overlay.addEventListener("click", function (event) {
		if (event.target === overlay) {
			closePopup();
		}
	});

	document.addEventListener("keydown", function (event) {
		if (!overlay.classList.contains("is-open")) {
			return;
		}
		if (event.key === "Escape") {
			closePopup();
		}
	});

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", function () {
			setTimeout(openPopup, 400);
		});
	} else {
		setTimeout(openPopup, 400);
	}
})();
