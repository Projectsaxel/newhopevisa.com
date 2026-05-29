(function () {
	"use strict";

	var STORAGE_KEY = "newhope-uscis-memo-2026-05-es-v1";

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
		'<button type="button" class="nhv-popup__close" aria-label="Cerrar aviso">&times;</button>' +
		'<div class="nhv-popup__header">' +
		'<h2 class="nhv-popup__title" id="nhv-uscis-popup-title">Memorando USCIS — Ajuste de Estatus</h2>' +
		'<p class="nhv-popup__subtitle">Publicado el 22 de mayo de 2026</p>' +
		"</div>" +
		'<div class="nhv-popup__body">' +
		'<p class="nhv-popup__greeting">Buenas tardes,</p>' +
		"<p>Nos gustar\u00eda compartir algunas aclaraciones importantes sobre el memorando publicado por USCIS el 22 de mayo de 2026, referente a los casos de Ajuste de Estatus.</p>" +
		"<p>El memorando refuerza que, de acuerdo con la Secci\u00f3n 245 del INA (Immigration and Nationality Act), el Ajuste de Estatus se considera un beneficio discrecional y extraordinario. Esto significa que, incluso cuando el extranjero cumple con los requisitos b\u00e1sicos de elegibilidad, la aprobaci\u00f3n del caso no es autom\u00e1tica. La decisi\u00f3n final depende del an\u00e1lisis y la discreci\u00f3n del oficial de inmigraci\u00f3n responsable del caso.</p>" +
		"<p>Seg\u00fan USCIS, siempre ha existido el entendimiento de que no todos los solicitantes elegibles tendr\u00e1n necesariamente aprobado su Ajuste de Estatus. El oficial puede evaluar las evidencias presentadas, el historial migratorio del solicitante y otros factores relevantes para determinar si la concesi\u00f3n del beneficio es apropiada y est\u00e1 en el mejor inter\u00e9s de los Estados Unidos.</p>" +
		"<p>El memorando tambi\u00e9n destaca que el Ajuste de Estatus no fue creado para reemplazar el proceso consular regular, sino para aplicarse \u00fanicamente a situaciones espec\u00edficas previstas por la ley.</p>" +
		"<p>Como resultado, despu\u00e9s de la entrevista y la revisi\u00f3n del caso, el solicitante puede recibir la aprobaci\u00f3n del Ajuste de Estatus o ser dirigido a continuar mediante procesamiento consular. Esto no significa necesariamente que la persona perder\u00e1 la oportunidad de obtener un estatus legal; sin embargo, el proceso puede volverse m\u00e1s largo y puede implicar costos adicionales.</p>" +
		"<p>En el proceso de revisi\u00f3n discrecional, USCIS instruye a los oficiales a considerar la totalidad de las circunstancias de cada caso, incluyendo factores positivos y negativos. Algunos de los factores que pueden ser revisados incluyen:</p>" +
		"<ul>" +
		"<li>violaciones migratorias o de estatus;</li>" +
		"<li>empleo no autorizado;</li>" +
		"<li>fraude o tergiversaci\u00f3n;</li>" +
		"<li>historial migratorio;</li>" +
		"<li>lazos familiares;</li>" +
		"<li>car\u00e1cter moral;</li>" +
		"<li>factores humanitarios y otras evidencias favorables.</li>" +
		"</ul>" +
		"<p>Aunque, en teor\u00eda, estas directrices siempre se han aplicado a los casos de Ajuste de Estatus, a\u00fan no sabemos exactamente c\u00f3mo este nuevo memorando afectar\u00e1 los casos que se encuentran actualmente pendientes. Sin embargo, entendemos que las revisiones de casos pueden volverse m\u00e1s detalladas y rigurosas en el futuro.</p>" +
		"<p>Continuaremos monitoreando las orientaciones de USCIS y mantendremos informados a nuestros clientes sobre cualquier cambio relevante.</p>" +
		'<p class="nhv-popup__signature">Atentamente,<br>New Hope Visa</p>' +
		"</div>" +
		'<div class="nhv-popup__footer">' +
		'<label class="nhv-popup__dismiss-label">' +
		'<input type="checkbox" id="nhv-uscis-popup-hide" />' +
		"No volver a mostrar" +
		"</label>" +
		'<button type="button" class="nhv-popup__btn" id="nhv-uscis-popup-ok">Entendido</button>' +
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
