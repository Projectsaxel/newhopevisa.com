"""Substituições EN→ES (e PT de UI) para páginas /es/."""

from __future__ import annotations

# Ordenar por tamanho decrescente no script
ES_REPLACEMENTS: dict[str, str] = {
	# Nav e header
	">Home</a>": ">Inicio</a>",
	">Services</a>": ">Servicios</a>",
	">Fee Schedule</a>": ">Tarifas</a>",
	">About Us</a>": ">Quiénes Somos</a>",
	">Contact Us</a>": ">Contacto</a>",
	"<span class=\"elementor-button-text\">Reserve</span>": "<span class=\"elementor-button-text\">Reservar</span>",
	"<span class=\"elementor-button-text\">Contact Us</span>": "<span class=\"elementor-button-text\">Contacto</span>",
	">Call Us</p>": ">Llámenos</p>",
	">Call Us</p>\t\t\t\t</div>": ">Llámenos</p>\t\t\t\t</div>",
	"aria-label=\"Menu\"": "aria-label=\"Menú\"",
	"aria-label=\"Alternar menu\"": "aria-label=\"Alternar menú\"",
	# Footer
	"<h4 class=\"elementor-heading-title elementor-size-default\">Menu</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Menú</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Contact</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Contacto</h4>",
	"<span class=\"elementor-icon-list-text\">Home</span>": "<span class=\"elementor-icon-list-text\">Inicio</span>",
	"<span class=\"elementor-icon-list-text\">Services</span>": "<span class=\"elementor-icon-list-text\">Servicios</span>",
	"<span class=\"elementor-icon-list-text\">Fee Schedule</span>": "<span class=\"elementor-icon-list-text\">Tarifas</span>",
	"<span class=\"elementor-icon-list-text\">About Us</span>": "<span class=\"elementor-icon-list-text\">Quiénes Somos</span>",
	"<span class=\"elementor-icon-list-text\">Contact Us</span>": "<span class=\"elementor-icon-list-text\">Contacto</span>",
	"<span class=\"elementor-icon-list-text\">Privacy Policy</span>": "<span class=\"elementor-icon-list-text\">Política de Privacidad</span>",
	"New Hope Immigration Services is a nonprofit dedicated to providing low-cost immigration and legal document preparation for low-income communities. Since 2018, our multilingual team has supported clients with asylum, TPS, DACA, VAWA, U Visa, work permits, family petitions, naturalization, and other key processes, as well as legal documents such as powers of attorney, guardianship, and translations.": (
		"New Hope Immigration Services es una organización sin fines de lucro dedicada a ofrecer preparación de documentos legales y de inmigración a bajo costo para comunidades de bajos ingresos. Desde 2018, nuestro equipo multilingüe ha apoyado a clientes con asilo, TPS, DACA, VAWA, visa U, permisos de trabajo, peticiones familiares, naturalización y otros procesos clave, además de documentos como poderes notariales, tutela y traducciones."
	),
	# Services page
	"<h1 class=\"elementor-heading-title elementor-size-default\">Services</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Servicios</h1>",
	"<h5 class=\"elementor-heading-title elementor-size-default\">ALL SERVICES</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">TODOS LOS SERVICIOS</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Seamless Immigration Solutions</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Soluciones Migratorias Integrales</h2>",
	"Explore our comprehensive range of exceptional services and unwavering commitment to excellence": (
		"Explora nuestra amplia gama de servicios excepcionales y nuestro compromiso inquebrantable con la excelencia"
	),
	"<a href=\"../peticion-familiar/\">Family Petitions\n</a>": "<a href=\"../peticion-familiar/\">Peticiones Familiares\n</a>",
	"<a href=\"../peticion-familiar/\">Family Petitions</a>": "<a href=\"../peticion-familiar/\">Peticiones Familiares</a>",
	"<a href=\"../ajuste-de-estatus/\">Adjustment of Status</a>": "<a href=\"../ajuste-de-estatus/\">Ajuste de Estatus</a>",
	"<a href=\"../procesamiento-consular/\">Consular Processing </a>": "<a href=\"../procesamiento-consular/\">Procesamiento Consular </a>",
	"<a href=\"../naturalizacion/\">Naturalization </a>": "<a href=\"../naturalizacion/\">Naturalización </a>",
	"<a href=\"../renovacion-de-residencia-i-90/\">Residence Renewals (I-90) </a>": "<a href=\"../renovacion-de-residencia-i-90/\">Renovación de Residencia (I-90) </a>",
	"<a href=\"../documentos-de-viaje/\">Travel Documents</a>": "<a href=\"../documentos-de-viaje/\">Documentos de Viaje</a>",
	"<a href=\"../estatus-de-proteccion-temporal-tps/\">Temporary Protected Status (TPS) </a>": "<a href=\"../estatus-de-proteccion-temporal-tps/\">Estatus de Protección Temporal (TPS) </a>",
	"<a href=\"../permiso-de-trabajo/\">Work Permit</a>": "<a href=\"../permiso-de-trabajo/\">Permiso de Trabajo</a>",
	"Personalized support to reunite families and secure lawful U.S. residency": (
		"Apoyo personalizado para reunir familias y asegurar la residencia legal en EE. UU."
	),
	"Guided assistance to help you transition smoothly to permanent residency": (
		"Asistencia guiada para ayudarte a pasar sin contratiempos a la residencia permanente"
	),
	"End-to-end support for visa application through U.S. consulates abroad": (
		"Apoyo integral para solicitudes de visa en consulados de EE. UU. en el exterior"
	),
	"Expert help preparing your path toward full U.S. citizenship with confidence": (
		"Ayuda experta para preparar tu camino hacia la ciudadanía estadounidense con confianza"
	),
	"Fast and reliable service for renewing or replacing your green card": (
		"Servicio rápido y confiable para renovar o reemplazar tu green card"
	),
	"Secure and professional assistance to obtain your advance parole for travel": (
		"Asistencia segura y profesional para obtener tu advance parole de viaje"
	),
	"Confidential, compassionate support for victims seeking legal protection": (
		"Apoyo confidencial y compasivo para víctimas que buscan protección legal"
	),
	"Comprehensive help applying or renewing TPS to maintain your legal stay": (
		"Ayuda integral para solicitar o renovar el TPS y mantener tu estancia legal"
	),
	"Strategic, detailed assistance to overcome immigration barriers": (
		"Asistencia estratégica y detallada para superar barreras migratorias"
	),
	"Efficient filing and follow-up for your Employment Authorization Document (EAD)": (
		"Presentación eficiente y seguimiento de tu Employment Authorization Document (EAD)"
	),
	"<h5 class=\"elementor-heading-title elementor-size-default\">BUSINESS INSIGHTS AND BEYOND</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">PERSPECTIVAS Y MÁS ALLÁ</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Your Trusted Immigration Partner</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Tu Socio Migratorio de Confianza</h2>",
	"In a rapidly evolving world, the only constant is change especially in the complex and ever-shifting landscape of immigration law and policy. It's no longer enough to simply keep pace, we must be ready to adapt quickly and proactively. Our team stays closely connected to every new update, regulation, and legal development, continuously refining our knowledge to ensure that we provide guidance that is accurate, current, and truly aligned with your needs.": (
		"En un mundo que evoluciona rápidamente, el único constante es el cambio, especialmente en el panorama complejo de las leyes y políticas de inmigración. Ya no basta con seguir el ritmo: debemos adaptarnos con rapidez y de forma proactiva. Nuestro equipo se mantiene al día con cada actualización, regulación y desarrollo legal para ofrecer orientación precisa, actual y alineada con tus necesidades."
	),
	"In a rapidly evolving world, the only constant is change especially in the complex and ever-shifting landscape of immigration law and policy. It\u2019s no longer enough to simply keep pace, we must be ready to adapt quickly and proactively. Our team stays closely connected to every new update, regulation, and legal development, continuously refining our knowledge to ensure that we provide guidance that is accurate, current, and truly aligned with your needs.": (
		"En un mundo que evoluciona rápidamente, el único constante es el cambio, especialmente en el panorama complejo de las leyes y políticas de inmigración. Ya no basta con seguir el ritmo: debemos adaptarnos con rapidez y de forma proactiva. Nuestro equipo se mantiene al día con cada actualización, regulación y desarrollo legal para ofrecer orientación precisa, actual y alineada con tus necesidades."
	),
	"Name							</label>": "Nombre							</label>",
	"Surname							</label>": "Apellido							</label>",
	"Email							</label>": "Correo electrónico							</label>",
	"Message							</label>": "Mensaje							</label>",
	'placeholder="Email"': 'placeholder="Correo electrónico"',
	'aria-label="Contact"': 'aria-label="Contacto"',
	'name="Contact"': 'name="Contacto"',
	'&quot;step_next_label&quot;:&quot;Next&quot;': '&quot;step_next_label&quot;:&quot;Siguiente&quot;',
	'&quot;step_previous_label&quot;:&quot;Previous&quot;': '&quot;step_previous_label&quot;:&quot;Anterior&quot;',
	'"inLanguage":"en"': '"inLanguage":"es"',
	"<h5 class=\"elementor-heading-title elementor-size-default\">Exploring Strategies</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">Explorando Estrategias</h5>",
	"Join us on this insightful journey as we uncover the tactics that drive progress.": (
		"Acompáñanos en este viaje para descubrir las tácticas que impulsan el progreso."
	),
	"<h5 class=\"elementor-heading-title elementor-size-default\">Passport to Possibilities</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">Pasaporte a las Posibilidades</h5>",
	"We dive into the world of effective planning, execution, and success in various fields.": (
		"Exploramos la planificación, la ejecución y el éxito en distintos ámbitos."
	),
	# About us
	"<h1 class=\"elementor-heading-title elementor-size-default\">About Us</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Quiénes Somos</h1>",
	"<h5 class=\"elementor-heading-title elementor-size-default\"> Service in Every Detail</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\"> Servicio en Cada Detalle</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Trusted Immigration Partner</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Socio Migratorio de Confianza</h2>",
	"Embark on a journey with us  that began with a vision. Our relentless pursuit of excellence has transformed this vision into a reality, shaping our business to not only meet but exceed your expectations.": (
		"Embárcate en un viaje con nosotros que comenzó con una visión. Nuestra búsqueda incansable de la excelencia transformó esa visión en realidad, moldeando nuestro trabajo para no solo cumplir, sino superar tus expectativas."
	),
	"Integrity, innovation, and a customer-centric approach are the cornerstones of our identity. We believe in doing business with transparency, accountability, and a constant drive for improvement. Beyond products and services, we are in the business of building connections. Whether you're a valued client, a potential partner, or a member of our community.": (
		"La integridad, la innovación y un enfoque centrado en el cliente son los pilares de nuestra identidad. Creemos en hacer negocios con transparencia, responsabilidad y mejora continua. Más allá de productos y servicios, construimos conexiones, ya seas cliente, socio o parte de nuestra comunidad."
	),
	"<h2 class=\"elementor-heading-title elementor-size-default\">Immigration\nSupport</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Apoyo en\nInmigración</h2>",
	"Flexibility and adaptability are key when implementing project management principles across diverse industries and contexts.": (
		"La flexibilidad y la adaptabilidad son clave al aplicar principios de gestión en distintos sectores y contextos."
	),
	"<span class=\"elementor-icon-list-text\">Fixed Budget</span>": "<span class=\"elementor-icon-list-text\">Presupuesto Fijo</span>",
	"<span class=\"elementor-icon-list-text\">Quality Assurance</span>": "<span class=\"elementor-icon-list-text\">Garantía de Calidad</span>",
	"<span class=\"elementor-icon-list-text\">Customization</span>": "<span class=\"elementor-icon-list-text\">Personalización</span>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Empowering Excellence</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Impulsando la Excelencia</h2>",
	"Your success, our commitment! Unlocking the potential of your product with innovative solutions and unwavering dedication to your success!": (
		"¡Tu éxito, nuestro compromiso! Desbloqueamos el potencial de tu caso con soluciones innovadoras y dedicación total."
	),
	"<span class=\"elementor-button-text\">View All</span>": "<span class=\"elementor-button-text\">Ver Todo</span>",
	"<h5 class=\"elementor-heading-title elementor-size-default\">REACH OUT AND CONNECT</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">CONTÁCTANOS</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Let's Stay in Touch</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Mantengámonos en Contacto</h2>",
	"Your bridge to meaningful communication and personalized assistance, we're here to listen and assist you": (
		"Tu puente hacia una comunicación significativa y asistencia personalizada; estamos aquí para escucharte y ayudarte"
	),
	"<span class=\"elementor-button-text\">Send</span>": "<span class=\"elementor-button-text\">Enviar</span>",
	# Contact
	"<h1 class=\"elementor-heading-title elementor-size-default\">Contact Us</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Contacto</h1>",
	'value="Contact Us - New Hope"': 'value="Contacto - New Hope"',
	'value="About Us - New Hope"': 'value="Quiénes Somos - New Hope"',
	"<h5 class=\"elementor-heading-title elementor-size-default\">DIRECT COMMUNICATION</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">COMUNICACIÓN DIRECTA</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Connect with Us</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Conéctate con Nosotros</h2>",
	"<h5 class=\"elementor-heading-title elementor-size-default\">WE'RE HERE TO LISTEN, ASSIST, AND BUILD RELATIONSHIPS</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">ESTAMOS AQUÍ PARA ESCUCHAR, AYUDAR Y CREAR VÍNCULOS</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Connect with Our Team</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Habla con Nuestro Equipo</h2>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Position :</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Dirección:</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Timetables :</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Horario:</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Contacts :</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Teléfono:</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Write Us :</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Escríbenos:</h4>",
	"<label for=\"form-field-name\" class=\"elementor-field-label\">Name</label>": "<label for=\"form-field-name\" class=\"elementor-field-label\">Nombre</label>",
	"<label for=\"form-field-field_9e095be\" class=\"elementor-field-label\">Surname</label>": "<label for=\"form-field-field_9e095be\" class=\"elementor-field-label\">Apellido</label>",
	"<label for=\"form-field-email\" class=\"elementor-field-label\">Email</label>": "<label for=\"form-field-email\" class=\"elementor-field-label\">Correo electrónico</label>",
	"<label for=\"form-field-message\" class=\"elementor-field-label\">Message</label>": "<label for=\"form-field-message\" class=\"elementor-field-label\">Mensaje</label>",
	"placeholder=\"Name\"": "placeholder=\"Nombre\"",
	"placeholder=\"Surname\"": "placeholder=\"Apellido\"",
	"placeholder=\"Message\"": "placeholder=\"Mensaje\"",
	# Fee schedule
	"<h2 class=\"elementor-heading-title elementor-size-default\">Fee Schedule</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Tarifas</h2>",
	"<span class=\"elementor-heading-title elementor-size-default\">Fees below does not include USCIS filing fees</span>": "<span class=\"elementor-heading-title elementor-size-default\">Las tarifas no incluyen las tasas de presentación del USCIS</span>",
	"<span class=\"elementor-button-text\">Service fee</span>": "<span class=\"elementor-button-text\">Tarifa del servicio</span>",
	"Receive personalized immigration guidance to understand your options, prepare documents, and plan your next steps confidently.": (
		"Recibe orientación migratoria personalizada para entender tus opciones, preparar documentos y planificar tus próximos pasos con confianza."
	),
	# Home (complementar es/index parcial)
	"<title>Home - New Hope</title>": "<title>Inicio - New Hope</title>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Trusted Immigration Services</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Servicios Migratorios de Confianza</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Most Common Services</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Servicios Más Comunes</h2>",
	"<h5 class=\"elementor-heading-title elementor-size-default\">PREDICTIONS AND PROJECTIONS</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">PROYECCIONES Y TENDENCIAS</h5>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">PREDICTIONS AND PROJECTIONS</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">PROYECCIONES Y TENDENCIAS</h2>",
	"<h5 class=\"elementor-heading-title elementor-size-default\"> Servicio en Cada Detalle</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">Servicio en Cada Detalle</h5>",
	"if you have a US Citizen relative, you may be eligible for family petition. Check your eligibility": (
		"Si tiene un familiar ciudadano estadounidense, puede ser elegible para una petición familiar. Verifique su elegibilidad."
	),
	"becoming a legal permanent resident? Adjustment of Status is the process that allows eligible individuals already in the United States to apply for lawful permanent residence without needing to return to their home country. Our team guides you through every step from document preparation to final approval, ensuring a smooth and worry-free path to obtaining your Green Card": (
		"¿Quiere convertirse en residente permanente legal? El ajuste de estatus permite que personas elegibles que ya están en EE. UU. soliciten la residencia permanente sin regresar a su país de origen. Nuestro equipo le guía en cada paso, desde la preparación de documentos hasta la aprobación final, para obtener su green card con tranquilidad."
	),
	"guidance through the U.S. citizenship application process, including documentation and eligibility requirements": (
		"Orientación durante todo el proceso de solicitud de ciudadanía estadounidense, incluyendo documentación y requisitos de elegibilidad."
	),
	"completing and tracking the renewal of your Permanent Resident Card": (
		"Completar y dar seguimiento a la renovación de su tarjeta de residente permanente."
	),
	"Our team of visa experts provides clear, reliable, and step-by-step guidance for every type of visa process. From student and religious visas to family-based or work-related applications, we ensure that all forms and requirements are completed accurately and on time.": (
		"Nuestro equipo de expertos en visas ofrece orientación clara, confiable y paso a paso para todo tipo de proceso. Desde visas de estudiante y religiosas hasta solicitudes familiares o laborales, nos aseguramos de que formularios y requisitos se completen con precisión y a tiempo."
	),
	"We help you understand each visa category, we organize your documents, and prepare your case with confidence. With our experience and dedication, you can trust that your application is handled with care and attention to every detail.": (
		"Le ayudamos a entender cada categoría de visa, organizamos sus documentos y preparamos su caso con confianza. Con nuestra experiencia y dedicación, puede confiar en que su solicitud se gestiona con cuidado y atención a cada detalle."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">Cost-Effective</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Relación calidad-precio</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Flexible Scheduling</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Horarios flexibles</h4>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Tailored Solutions</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Soluciones a su medida</h2>",
	"Every immigration journey is unique — that's why we offer tailored solutions designed around your specific goals. Whether you need help with family petitions, visa changes, or document preparation, our team creates a personalized plan that fits your needs.": (
		"Cada trayectoria migratoria es única; por eso ofrecemos soluciones diseñadas según sus objetivos. Ya sea peticiones familiares, cambios de visa o preparación de documentos, creamos un plan personalizado para usted."
	),
	"Every immigration journey is unique — that’s why we offer tailored solutions designed around your specific goals. Whether you need help with family petitions, visa changes, or document preparation, our team creates a personalized plan that fits your needs.": (
		"Cada trayectoria migratoria es única; por eso ofrecemos soluciones diseñadas según sus objetivos. Ya sea peticiones familiares, cambios de visa o preparación de documentos, creamos un plan personalizado para usted."
	),
	"We take the time to understand your situation and provide the right guidance for each step. With customized support and clear communication, we help you move forward confidently toward your life and career in the United States.": (
		"Dedicamos tiempo a entender su situación y ofrecer la orientación adecuada en cada paso. Con apoyo personalizado y comunicación clara, le ayudamos a avanzar con confianza hacia su vida y carrera en Estados Unidos."
	),
	"<h5 class=\"elementor-heading-title elementor-size-default\">Popular services</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">Servicios populares</h5>",
	"Receive personalized immigration guidance to understand your options, and plan your next steps confidently": (
		"Reciba orientación migratoria personalizada para entender sus opciones y planificar sus próximos pasos con confianza"
	),
	"Get professional assistance to extend your visitor visa stay in the U.S., ensuring your forms are accurate and submitted on time": (
		"Obtenga asistencia profesional para extender su estancia con visa de visitante en EE. UU., con formularios correctos y a tiempo"
	),
	"Smoothly transition from visitor to student or dependent status with step-by-step support and complete document prep": (
		"Haga la transición de visitante a estudiante o dependiente con apoyo paso a paso y documentación completa"
	),
	"<h5 class=\"elementor-heading-title elementor-size-default\">Our Clients</h5>": "<h5 class=\"elementor-heading-title elementor-size-default\">Nuestros clientes</h5>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Students</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Estudiantes</h4>",
	"Who need help applying for or changing to F1/F2 visas": (
		"Que necesitan ayuda para solicitar o cambiar a visas F1/F2"
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">New immigrants</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Nuevos inmigrantes</h4>",
	"Who recently arrived and need help understanding U.S. immigration system": (
		"Que llegaron recientemente y necesitan ayuda para entender el sistema de inmigración de EE. UU."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">Citizenship applicants</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Solicitantes de ciudadanía</h4>",
	"Preparing for the naturalization process": "Preparándose para el proceso de naturalización",
	"<h4 class=\"elementor-heading-title elementor-size-default\">Families</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Familias</h4>",
	"Looking to reunite with loved ones through family petition": (
		"Que desean reunirse con sus seres queridos mediante una petición familiar"
	),
	"Empowering your dreams, one step at a time. Experience excellence with us, where innovation meets customer satisfaction with custom solutions for you.": (
		"Impulsando sus sueños, paso a paso. Experimente la excelencia con nosotros, donde la innovación se une a la satisfacción del cliente con soluciones personalizadas."
	),
	"<span class=\"elementor-button-text\">Taxa</span>": "<span class=\"elementor-button-text\">Tarifa</span>",
	"<span class=\"elementor-button-text\">Saber Más</span>": "<span class=\"elementor-button-text\">Saber más</span>",
	"<span class=\"elementor-button-text\">Comenzar Ahora</span>": "<span class=\"elementor-button-text\">Comenzar ahora</span>",
	# Elementor (strings PT no JS → ES)
	'"a11yCarouselPrevSlideMessage":"Slide anterior"': '"a11yCarouselPrevSlideMessage":"Diapositiva anterior"',
	'"a11yCarouselNextSlideMessage":"Pr\\u00f3ximo slide"': '"a11yCarouselNextSlideMessage":"Siguiente diapositiva"',
	'"a11yCarouselFirstSlideMessage":"Este \\u00e9 o primeiro slide"': '"a11yCarouselFirstSlideMessage":"Esta es la primera diapositiva"',
	'"a11yCarouselLastSlideMessage":"Este \\u00e9 o \\u00faltimo slide"': '"a11yCarouselLastSlideMessage":"Esta es la última diapositiva"',
	'"a11yCarouselPaginationBulletMessage":"Ir para o slide"': '"a11yCarouselPaginationBulletMessage":"Ir a la diapositiva"',
	'"label":"Dispositivos m\\u00f3veis no modo retrato"': '"label":"Móviles en modo vertical"',
	'"label":"Dispositivos m\\u00f3veis no modo paisagem"': '"label":"Móviles en modo horizontal"',
	'"label":"Tablet no modo retrato"': '"label":"Tablet en modo vertical"',
	'"label":"Tablet no modo paisagem"': '"label":"Tablet en modo horizontal"',
	'"label":"Dispositivos m\\u00f3veis"': '"label":"Dispositivos móviles"',
	"<h2 class=\"elementor-heading-title elementor-size-default\">Visa Experts</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Expertos en Visas</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Global Horizons</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Horizontes Globales</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">People We Support</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Personas a las que Apoyamos</h2>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Crafting Real Solutions for Immigration Needs</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Soluciones Reales para tus Necesidades Migratorias</h1>",
	"Our team of visa experts provides clear, reliable guidance to help you navigate every step of your immigration journey with confidence.": (
		"Nuestro equipo de expertos en visas ofrece orientación clara y confiable para ayudarte a recorrer cada paso de tu proceso migratorio con seguridad."
	),
	"Every immigration journey is unique. We offer tailored support to help you move forward with clarity and peace of mind.": (
		"Cada proceso migratorio es único. Ofrecemos apoyo personalizado para que avances con claridad y tranquilidad."
	),
	"Support designed for every immigration journey.": "Apoyo diseñado para cada trayectoria migratoria.",
	"<span class=\"elementor-button-text\">More Info</span>": "<span class=\"elementor-button-text\">Más Información</span>",
	"<span class=\"elementor-button-text\">Find Out More</span>": "<span class=\"elementor-button-text\">Saber Más</span>",
	"<span class=\"elementor-button-text\">Start Now</span>": "<span class=\"elementor-button-text\">Comenzar Ahora</span>",
	"Family petitions": "Peticiones familiares",
	"Adjustment of status": "Ajuste de estatus",
	"Naturalization": "Naturalización",
	"Green Card renewal": "Renovación de Green Card",
	"Consultation": "Consulta",
	"Extension of Status (B1/B2)": "Extensión de Estatus (B1/B2)",
	# Service page H1s
	"<h1 class=\"elementor-heading-title elementor-size-default\">Work Permit</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Permiso de Trabajo</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Waivers</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Waivers</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">VAWA</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">VAWA</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Travel Documents</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Documentos de Viaje</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Family Petitions</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Peticiones Familiares</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Adjustment of Status</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Ajuste de Estatus</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Consular Processing</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Procesamiento Consular</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Naturalization</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Naturalización</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Residence Renewals (I-90)</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Renovación de Residencia (I-90)</h1>",
	"<h1 class=\"elementor-heading-title elementor-size-default\">Temporary Protected Status (TPS)</h1>": "<h1 class=\"elementor-heading-title elementor-size-default\">Estatus de Protección Temporal (TPS)</h1>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Work Permit</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Permiso de Trabajo</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Waivers</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Waivers</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">VAWA</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">VAWA</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Travel Documents</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Documentos de Viaje</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Family Petitions</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Peticiones Familiares</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Adjustment of Status</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Ajuste de Estatus</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Consular Processing</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Procesamiento Consular</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Naturalization</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Naturalización</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Residence Renewals (I-90)</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Renovación de Residencia (I-90)</h2>",
	"<h2 class=\"elementor-heading-title elementor-size-default\">Temporary Protected Status (TPS)</h2>": "<h2 class=\"elementor-heading-title elementor-size-default\">Estatus de Protección Temporal (TPS)</h2>",
	# Elementor i18n (footer scripts)
	'"shareOnFacebook":"Compartilhar no Facebook"': '"shareOnFacebook":"Compartir en Facebook"',
	'"shareOnTwitter":"Compartilhar no Twitter"': '"shareOnTwitter":"Compartir en Twitter"',
	'"pinIt":"Fixar"': '"pinIt":"Fijar"',
	'"download":"Baixar"': '"download":"Descargar"',
	'"downloadImage":"Baixar imagem"': '"downloadImage":"Descargar imagen"',
	'"fullscreen":"Tela cheia"': '"fullscreen":"Pantalla completa"',
	'"share":"Compartilhar"': '"share":"Compartir"',
	'"playVideo":"Reproduzir v\\u00eddeo"': '"playVideo":"Reproducir video"',
	'"previous":"Anterior"': '"previous":"Anterior"',
	'"next":"Pr\\u00f3ximo"': '"next":"Siguiente"',
	'"close":"Fechar"': '"close":"Cerrar"',
	# Tarifas (fee-schedule) — títulos e descrições
	"Get professional assistance to extend your visitor visa stay in the U.S., ensuring your forms are accurate and submitted on time.": (
		"Obtén asistencia profesional para extender tu estancia con visa de visitante en EE. UU., con formularios correctos y a tiempo."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">Change of Status (B1/B2 to F1/F2)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Cambio de Estatus (B1/B2 a F1/F2)</h4>",
	"Smoothly transition from visitor to student or dependent status with step-by-step support and complete document prep.": (
		"Transición fluida de visitante a estudiante o dependiente, con apoyo paso a paso y documentación completa."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">CORRECTION OF I94 INQUIRY</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Corrección de consulta I-94</h4>",
	"Assistance with inquiries and corrections related to your I-94 record.": (
		"Asistencia con consultas y correcciones relacionadas con su registro I-94."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">FOIA REQUEST </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Solicitud FOIA</h4>",
	"Support in submitting and managing your FOIA request for official immigration records.": (
		"Apoyo para presentar y gestionar su solicitud FOIA de registros oficiales de inmigración."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">ADJUSTMENT OF STATUS WITH APPROVED PETITION</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Ajuste de estatus con petición aprobada</h4>",
	"Guidance and support for the Adjustment of Status process based on your approved petition.": (
		"Orientación y apoyo en el proceso de ajuste de estatus según su petición aprobada."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">ADJUSTMENT OF STATUS ALONG WITH I130 PETITION</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Ajuste de estatus con petición I-130</h4>",
	"Comprehensive assistance with the Adjustment of Status process filed concurrently with the I-130 petition.": (
		"Asistencia integral en el ajuste de estatus presentado junto con la petición I-130."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">NATURALIZATION PROCESS</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Proceso de naturalización</h4>",
	"Guidance and support throughout the Naturalización process to obtain U.S. citizenship.": (
		"Orientación y apoyo durante todo el proceso de naturalización para obtener la ciudadanía estadounidense."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">IMMEDIATE RELATIVE PETITION\t(ONE STEP) (I-130)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Petición de familiar inmediato (un paso) (I-130)</h4>",
	"Complete assistance with the Immediate Relative Petition (One Step) through filing and processing the I-130 petition.": (
		"Asistencia completa en la petición de familiar inmediato (un paso), incluyendo el I-130."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">FIANCEE VISA (ONE STEP)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Visa de prometido(a) (un paso)</h4>",
	"Comprehensive assistance with the Fiancée Visa (One Step) application process from start to finish.": (
		"Asistencia integral en la solicitud de visa de prometido(a) (un paso), de principio a fin."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">REMOVAL OF CONDITIONS (I751)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Eliminación de condiciones (I-751)</h4>",
	"Support with the Removal of Conditions process (I-751) to maintain your permanent resident status.": (
		"Apoyo en el proceso de eliminación de condiciones (I-751) para mantener su residencia permanente."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">RELIGIOUS VISA </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Visa religiosa</h4>",
	"Assistance with the application and processing of Religious Worker Visas.": (
		"Asistencia en la solicitud y tramitación de visas para trabajadores religiosos."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">CONSULATE PROCESS </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Proceso consular</h4>",
	"Guidance and support throughout the Consular Processing stage for immigrant and non-immigrant visa cases.": (
		"Orientación y apoyo en la etapa de procesamiento consular para visas de inmigrante y no inmigrante."
	),
	"Assistance with applying for and maintaining Temporary Protected Status (TPS).": (
		"Asistencia para solicitar y mantener el Estatus de Protección Temporal (TPS)."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">RENEWAL OF GREEN CARD (I-90)\t</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Renovación de green card (I-90)</h4>",
	"Support with the Renovación de Green Card process (I-90), from application to approval.": (
		"Apoyo en el proceso de renovación de green card (I-90), desde la solicitud hasta la aprobación."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">TRANSLATION </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Traducción</h4>",
	"Accurate and certified translation services for immigration and legal documents.": (
		"Servicios de traducción precisos y certificados para documentos legales y de inmigración."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">$30/page </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">$30/página</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">RFE RESPONSE (Not Clients)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Respuesta RFE (no clientes)</h4>",
	"Preparation of thorough, accurate, and fully compliant RFE responses for non-client cases.": (
		"Preparación de respuestas RFE completas y conformes para casos de no clientes."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">It Varies </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Varía</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">RFE RESPONSE (For clients)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Respuesta RFE (clientes)</h4>",
	"Preparation of comprehensive and compliant RFE responses for client cases.": (
		"Preparación de respuestas RFE integrales y conformes para clientes."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">From $150.00 </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Desde $150.00</h4>",
	"<h4 class=\"elementor-heading-title elementor-size-default\">EAD APPLICATION (I765 FORM)/ COMBO CARD Travel Doc</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Solicitud EAD (I-765) / Combo Card documento de viaje</h4>",
	"Assistance with the EAD application (Form I-765) and Combo Card (Travel Document) processing.": (
		"Asistencia con la solicitud EAD (Form I-765) y tramitación del Combo Card (documento de viaje)."
	),
	"Guidance and support throughout the VAWA self-petition process for eligible applicants.": (
		"Orientación y apoyo durante el proceso de autopetición VAWA para solicitantes elegibles."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">DACA RENEWAL plus EAD ( if needed)</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Renovación DACA más EAD (si aplica)</h4>",
	"Support with DACA renewal and EAD application when needed.": (
		"Apoyo con renovación DACA y solicitud EAD cuando sea necesario."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">I824 (TPS) Action on approved petition</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">I-824 (TPS) acción sobre petición aprobada</h4>",
	"Assistance with Form I-824 for TPS applicants seeking action on an approved petition.": (
		"Asistencia con el Form I-824 para solicitantes TPS que buscan acción sobre una petición aprobada."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">I601A WAIVER</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Waiver I-601A</h4>",
	"Guidance and support throughout the I-601A Provisional Unlawful Presence Waiver process.": (
		"Orientación y apoyo durante el proceso de waiver provisional I-601A por presencia ilegal."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">I212 WAIVER </h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">Waiver I-212</h4>",
	"Assistance with the I-212 waiver process for permission to reapply for admission into the United States.": (
		"Asistencia con el proceso de waiver I-212 para permiso de readmisión a Estados Unidos."
	),
	"<h4 class=\"elementor-heading-title elementor-size-default\">$1000 - PRO BONO case by case</h4>": "<h4 class=\"elementor-heading-title elementor-size-default\">$1000 - PRO BONO según caso</h4>",
}
