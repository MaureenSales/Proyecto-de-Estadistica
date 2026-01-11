# Diccionario de Variables BRFSS 2022
## Total: 326 columnas

---

# RESUMEN POR CATEGORÍAS

| Categoría | Cantidad | Columnas |
|-----------|----------|----------|
| Identificación y Muestreo | 32 | 1-32 |
| Estado de Salud | 4 | 33-36 |
| Acceso a Salud | 4 | 37-40 |
| Ejercicio y Sueño | 2 | 41-42 |
| Salud Oral | 2 | 43-44 |
| Condiciones Crónicas | 13 | 45-57 |
| Demografía | 11 | 58-68 |
| Medidas Físicas | 2 | 69-70 |
| Discapacidad | 6 | 71-76 |
| Detección Cáncer Mujeres | 7 | 77-83 |
| Detección Colorrectal | 13 | 84-96 |
| Tabaco y E-cigarrillos | 10 | 97-106 |
| Alcohol | 4 | 107-110 |
| Inmunizaciones | 4 | 111-114 |
| VIH | 3 | 115-117 |
| COVID-19 | 3 | 118-120 |
| Diabetes | 9 | 121-129 |
| Fatiga Crónica | 3 | 130-132 |
| Vacunas y EPOC | 10 | 133-145 |
| Supervivencia Cáncer | 13 | 146-158 |
| Próstata | 5 | 159-163 |
| Deterioro Cognitivo | 6 | 164-169 |
| Cuidadores | 10 | 170-178 |
| ACEs | 13 | 179-191 |
| Bienestar Social | 10 | 192-201 |
| Marihuana | 7 | 202-208 |
| Tabaco Extendido | 5 | 209-213 |
| Alcohol Screening | 5 | 214-218 |
| Armas de Fuego | 3 | 219-221 |
| Niños/Género | 10 | 222-231 |
| Planificación Familiar | 6 | 232-237 |
| Discriminación | 6 | 238-243 |
| Admin/Pesos | 19 | 244-262 |
| Variables Calculadas | 64 | 263-326 |

---

# DETALLE DE CADA VARIABLE

## SECCIÓN 1: IDENTIFICACIÓN Y MUESTREO (1-32)

| # | Variable | Descripción |
|---|----------|-------------|
| 1 | _STATE | Código FIPS del estado |
| 2 | FMONTH | Mes del archivo |
| 3 | IDATE | Fecha de entrevista (MMDDYYYY) |
| 4 | IMONTH | Mes de entrevista |
| 5 | IDAY | Día de entrevista |
| 6 | IYEAR | Año de entrevista (2022) |
| 7 | DISPCODE | Código de disposición final |
| 8 | SEQNO | Número de secuencia anual |
| 9 | _PSU | Unidad de muestreo primaria |
| 10 | CTELENM1 | ¿Número telefónico correcto? (línea fija) |
| 11 | PVTRESD1 | ¿Residencia privada? (línea fija) |
| 12 | COLGHOUS | ¿Vive en residencia universitaria? |
| 13 | STATERE1 | ¿Residente del estado? |
| 14 | CELPHON1 | ¿Es teléfono celular? |
| 15 | LADULT1 | ¿Tiene 18+ años? (línea fija) |
| 16 | COLGSEX1 | Sexo (residencia universitaria) |
| 17 | NUMADULT | Número de adultos en hogar |
| 18 | LANDSEX1 | Sexo del respondiente (línea fija) |
| 19 | NUMMEN | Número de hombres adultos |
| 20 | NUMWOMEN | Número de mujeres adultas |
| 21 | RESPSLCT | Respondiente seleccionado |
| 22 | SAFETIME | ¿Momento seguro para hablar? |
| 23 | CTELNUM1 | ¿Número correcto? (celular) |
| 24 | CELLFON5 | ¿Es celular? (verificación) |
| 25 | CADULT1 | ¿Tiene 18+ años? (celular) |
| 26 | CELLSEX1 | Sexo del respondiente (celular) |
| 27 | PVTRESD3 | ¿Residencia privada? (celular) |
| 28 | CCLGHOUS | ¿Residencia universitaria? (celular) |
| 29 | CSTATE1 | ¿Residente del estado? (celular) |
| 30 | LANDLINE | ¿Tiene línea fija? |
| 31 | HHADULT | Adultos en hogar (celular) |
| 32 | SEXVAR | Variable de sexo combinada |

---

## SECCIÓN 2: ESTADO DE SALUD GENERAL (33-36)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 33 | **GENHLTH** | Salud general autopercibida | 1=Excelente, 2=Muy buena, 3=Buena, 4=Regular, 5=Mala |
| 34 | **PHYSHLTH** | Días de mala salud física (30 días) | 1-30 días, 88=Ninguno |
| 35 | **MENTHLTH** | Días de mala salud mental (30 días) | 1-30 días, 88=Ninguno |
| 36 | **POORHLTH** | Días con actividad limitada | 1-30 días, 88=Ninguno |

---

## SECCIÓN 3: ACCESO A SERVICIOS DE SALUD (37-40)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 37 | PRIMINSR | Tipo principal de seguro de salud | 1-10 tipos, 88=Ninguno |
| 38 | PERSDOC3 | ¿Tiene médico personal? | 1=Sí uno, 2=Más de uno, 3=No |
| 39 | MEDCOST1 | ¿No pudo ver médico por costo? | 1=Sí, 2=No |
| 40 | CHECKUP1 | Tiempo desde último chequeo | 1=<1año, 2=1-2años, 3=2-5años, 4=>5años, 8=Nunca |

---

## SECCIÓN 4: EJERCICIO Y SUEÑO (41-42) ⭐

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 41 | EXERANY2 | ¿Hizo ejercicio en último mes? | 1=Sí, 2=No |
| 42 | **SLEPTIM1** | **Horas de sueño promedio en 24h** | **1-24 horas** |

---

## SECCIÓN 5: SALUD ORAL (43-44) 🆕

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 43 | LASTDEN4 | ¿Cuándo fue última visita al dentista? | 1=<1año, 2=1-2años, 3=2-5años, 4=>5años, 8=Nunca |
| 44 | RMVTETH4 | Dientes removidos por caries/enfermedad | 1=1-5, 2=6+, 3=Todos, 8=Ninguno |

---

## SECCIÓN 6: CONDICIONES CRÓNICAS (45-57)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 45 | CVDINFR4 | ¿Le dijeron que tuvo infarto? | 1=Sí, 2=No |
| 46 | CVDCRHD4 | ¿Le dijeron que tiene enfermedad coronaria? | 1=Sí, 2=No |
| 47 | CVDSTRK3 | ¿Le dijeron que tuvo derrame? | 1=Sí, 2=No |
| 48 | ASTHMA3 | ¿Le dijeron que tiene asma? | 1=Sí, 2=No |
| 49 | ASTHNOW | ¿Todavía tiene asma? | 1=Sí, 2=No |
| 50 | CHCSCNC1 | ¿Le dijeron que tiene cáncer de piel? | 1=Sí, 2=No |
| 51 | CHCOCNC1 | ¿Le dijeron que tiene otro cáncer? | 1=Sí, 2=No |
| 52 | CHCCOPD3 | ¿Le dijeron que tiene EPOC? | 1=Sí, 2=No |
| 53 | **ADDEPEV3** | **¿Le dijeron que tiene depresión?** | **1=Sí, 2=No** |
| 54 | CHCKDNY2 | ¿Le dijeron que tiene enfermedad renal? | 1=Sí, 2=No |
| 55 | HAVARTH4 | ¿Le dijeron que tiene artritis? | 1=Sí, 2=No |
| 56 | **DIABETE4** | **¿Le dijeron que tiene diabetes?** | **1=Sí, 2=Sí embarazo, 3=No, 4=Pre-diabetes** |
| 57 | DIABAGE4 | Edad de diagnóstico de diabetes | Edad en años |

---

## SECCIÓN 7: DEMOGRAFÍA (58-68)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 58 | **MARITAL** | Estado civil | 1=Casado, 2=Divorciado, 3=Viudo, 4=Separado, 5=Nunca casado, 6=Pareja |
| 59 | **EDUCA** | Nivel educativo | 1-6 (sin escuela a universidad) |
| 60 | RENTHOM1 | ¿Alquila o es propietario? | 1=Propietario, 2=Alquila, 3=Otro |
| 61 | NUMHHOL4 | ¿Más de un teléfono en hogar? | 1=Sí, 2=No |
| 62 | NUMPHON4 | Número de teléfonos | 1-6 |
| 63 | CPDEMO1C | ¿Tiene celular personal? | 1=Sí, 2=No |
| 64 | VETERAN3 | ¿Es veterano? | 1=Sí, 2=No |
| 65 | **EMPLOY1** | Situación laboral | 1=Empleado, 2=Autoempleado, 3-4=Desempleado, 5=Hogar, 6=Estudiante, 7=Retirado, 8=Incapacitado |
| 66 | **CHILDREN** | Niños <18 en hogar | 1-87 o 88=Ninguno |
| 67 | **INCOME3** | Ingreso anual del hogar | 1-11 categorías (hasta >$200K) |
| 68 | PREGNANT | ¿Está embarazada? | 1=Sí, 2=No |

---

## SECCIÓN 8: MEDIDAS FÍSICAS (69-70)

| # | Variable | Descripción |
|---|----------|-------------|
| 69 | **WEIGHT2** | Peso (libras o kg) |
| 70 | **HEIGHT3** | Altura (pies/pulgadas o metros) |

---

## SECCIÓN 9: DISCAPACIDAD (71-76)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 71 | DEAF | ¿Es sordo o tiene dificultad seria para oír? | 1=Sí, 2=No |
| 72 | BLIND | ¿Es ciego o tiene dificultad seria para ver? | 1=Sí, 2=No |
| 73 | DECIDE | ¿Dificultad para concentrarse/recordar/decidir? | 1=Sí, 2=No |
| 74 | DIFFWALK | ¿Dificultad seria para caminar/subir escaleras? | 1=Sí, 2=No |
| 75 | DIFFDRES | ¿Dificultad para vestirse/bañarse? | 1=Sí, 2=No |
| 76 | DIFFALON | ¿Dificultad para hacer mandados solo? | 1=Sí, 2=No |

---

## SECCIÓN 10: DETECCIÓN DE CÁNCER - MUJERES (77-83)

| # | Variable | Descripción |
|---|----------|-------------|
| 77 | HADMAM | ¿Ha tenido mamografía? |
| 78 | HOWLONG | ¿Hace cuánto fue la mamografía? |
| 79 | CERVSCRN | ¿Ha tenido examen cervical? |
| 80 | CRVCLCNC | ¿Le dijeron que tiene cáncer cervical? |
| 81 | CRVCLPAP | ¿Ha tenido Papanicolau? |
| 82 | CRVCLHPV | ¿Ha tenido prueba de VPH? |
| 83 | HADHYST2 | ¿Ha tenido histerectomía? |

---

## SECCIÓN 11: DETECCIÓN COLORRECTAL (84-96)

| # | Variable | Descripción |
|---|----------|-------------|
| 84 | HADSIGM4 | ¿Ha tenido sigmoidoscopia/colonoscopia? |
| 85 | COLNSIGM | Tipo de procedimiento (colonoscopia vs sigmoidoscopia) |
| 86 | COLNTES1 | ¿Cuántas colonoscopias ha tenido? |
| 87 | SIGMTES1 | ¿Cuántas sigmoidoscopias ha tenido? |
| 88 | LASTSIG4 | ¿Hace cuánto fue el último procedimiento? |
| 89 | COLNCNCR | ¿Resultado mostró cáncer/pólipos? |
| 90 | VIRCOLO1 | ¿Ha tenido colonoscopia virtual? |
| 91 | VCLNTES2 | ¿Hace cuánto fue la colonoscopia virtual? |
| 92 | SMALSTOL | ¿Ha tenido prueba de sangre oculta? |
| 93 | STOLTEST | Tipo de prueba de sangre oculta |
| 94 | STOOLDN2 | ¿Hace cuánto fue la prueba? |
| 95 | BLDSTFIT | ¿Prueba de sangre oculta FIT? |
| 96 | SDNATES1 | ¿Prueba de ADN en heces? |

---

## SECCIÓN 12: TABACO Y E-CIGARRILLOS (97-106)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 97 | **SMOKE100** | ¿Ha fumado 100+ cigarrillos en su vida? | 1=Sí, 2=No |
| 98 | **SMOKDAY2** | ¿Fuma actualmente? | 1=Todos los días, 2=Algunos días, 3=Nunca |
| 99 | USENOW3 | ¿Usa tabaco sin humo? | 1=Todos los días, 2=Algunos días, 3=Nunca |
| 100 | **ECIGNOW2** | **¿Usa cigarrillos electrónicos?** 🆕 | **1=Todos los días, 2=Algunos días, 3=Nunca** |
| 101 | LCSFIRST | Edad cuando fumó primer cigarrillo |
| 102 | LCSLAST | ¿Hace cuánto fue el último cigarrillo? |
| 103 | LCSNUMCG | Número de cigarrillos por día |
| 104 | LCSCTSC1 | ¿Ha tenido CT scan de pulmón? |
| 105 | LCSSCNCR | ¿CT scan mostró cáncer? |
| 106 | LCSCTWHN | ¿Hace cuánto fue el CT scan? |

---

## SECCIÓN 13: ALCOHOL (107-110)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 107 | **ALCDAY4** | Días con alcohol en últimos 30 | 1XX=días/semana, 2XX=días/mes |
| 108 | **AVEDRNK3** | Promedio de bebidas por ocasión | 1-76 |
| 109 | **DRNK3GE5** | Veces con 5+ bebidas (30 días) | 1-76, 88=Ninguna |
| 110 | **MAXDRNKS** | Máximo bebidas en una ocasión | 1-76 |

---

## SECCIÓN 14: INMUNIZACIONES (111-114)

| # | Variable | Descripción |
|---|----------|-------------|
| 111 | FLUSHOT7 | ¿Vacuna de gripe en últimos 12 meses? |
| 112 | FLSHTMY3 | Mes/año de última vacuna de gripe |
| 113 | PNEUVAC4 | ¿Ha recibido vacuna de neumonía? |
| 114 | TETANUS1 | ¿Ha recibido vacuna de tétanos? |

---

## SECCIÓN 15: VIH (115-117)

| # | Variable | Descripción |
|---|----------|-------------|
| 115 | HIVTST7 | ¿Se ha hecho prueba de VIH? |
| 116 | HIVTSTD3 | Mes/año de última prueba VIH |
| 117 | HIVRISK5 | Comportamientos de riesgo VIH |

---

## SECCIÓN 16: COVID-19 (118-120) 🆕

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 118 | **COVIDPOS** | **¿Ha dado positivo a COVID-19?** | **1=Sí, 2=No** |
| 119 | COVIDSMP | ¿Tuvo síntomas de COVID-19? |
| 120 | COVIDPRM | ¿Tiene síntomas prolongados (Long COVID)? |

---

## SECCIÓN 17: DIABETES - MÓDULO (121-129)

| # | Variable | Descripción |
|---|----------|-------------|
| 121 | PDIABTS1 | ¿Prueba de diabetes en últimos 3 años? |
| 122 | PREDIAB2 | ¿Le dijeron que tiene pre-diabetes? |
| 123 | DIABTYPE | Tipo de diabetes (1 o 2) 🆕 |
| 124 | INSULIN1 | ¿Usa insulina? |
| 125 | CHKHEMO3 | Veces que le revisaron A1C |
| 126 | EYEEXAM1 | Último examen de ojos dilatados |
| 127 | DIABEYE1 | ¿Diabetes afectó sus ojos? |
| 128 | DIABEDU1 | ¿Tomó curso de manejo de diabetes? |
| 129 | FEETSORE | ¿Tiene llagas en los pies? |

---

## SECCIÓN 18: FATIGA CRÓNICA (130-132) 🆕

| # | Variable | Descripción |
|---|----------|-------------|
| 130 | TOLDCFS | ¿Le dijeron que tiene síndrome de fatiga crónica? |
| 131 | HAVECFS | ¿Todavía tiene fatiga crónica? |
| 132 | WORKCFS | ¿La fatiga afecta su trabajo? |

---

## SECCIÓN 19: VACUNAS Y EPOC (133-145)

| # | Variable | Descripción |
|---|----------|-------------|
| 133 | IMFVPLA3 | Lugar donde recibió vacuna de gripe |
| 134 | HPVADVC4 | ¿Médico recomendó vacuna VPH? |
| 135 | HPVADSHT | ¿Recibió vacuna VPH? |
| 136 | SHINGLE2 | ¿Recibió vacuna de herpes zóster? |
| 137 | **COVIDVA1** | **¿Recibió vacuna COVID-19?** 🆕 |
| 138 | COVIDNU1 | Número de dosis COVID-19 |
| 139 | COVIDFS1 | Fecha de primera dosis COVID |
| 140 | COVIDSE1 | Efectos secundarios de vacuna COVID |
| 141 | COPDCOGH | ¿Tos persistente? (EPOC) |
| 142 | COPDFLEM | ¿Flema persistente? |
| 143 | COPDBRTH | ¿Dificultad para respirar? |
| 144 | COPDBTST | ¿Prueba de EPOC? |
| 145 | COPDSMOK | ¿Fumó contribuyó a EPOC? |

---

## SECCIÓN 20: SUPERVIVENCIA DE CÁNCER (146-158)

| # | Variable | Descripción |
|---|----------|-------------|
| 146 | CNCRDIFF | ¿Dificultades por cáncer? |
| 147 | CNCRAGE | Edad de diagnóstico de cáncer |
| 148 | CNCRTYP2 | Tipo de cáncer |
| 149-158 | CSRVTRT3-CSRVCTL2 | Tratamiento, seguimiento, dolor, etc. |

---

## SECCIÓN 21: PRÓSTATA (159-163)

| # | Variable | Descripción |
|---|----------|-------------|
| 159 | PSATEST1 | ¿Se ha hecho prueba PSA? |
| 160 | PSATIME1 | ¿Hace cuánto fue la prueba? |
| 161 | PCPSARS2 | Razón para hacerse la prueba |
| 162 | PSASUGST | ¿Médico sugirió la prueba? |
| 163 | PCSTALK1 | ¿Habló con médico sobre PSA? |

---

## SECCIÓN 22: DETERIORO COGNITIVO (164-169)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 164 | **CIMEMLOS** | Confusión/pérdida de memoria que empeora | 1=Sí, 2=No |
| 165 | CDHOUSE | ¿Ha dejado actividades por confusión? | 1=Siempre, 2=Usualmente, 3=A veces, 4=Rara vez, 5=Nunca |
| 166 | CDASSIST | ¿Necesita ayuda con actividades diarias? | Misma escala |
| 167 | CDHELP | ¿Necesita ayuda de otros? | 1=Sí, 2=No |
| 168 | CDSOCIAL | ¿Interfiere con actividades sociales? | 1=Siempre a 5=Nunca |
| 169 | CDDISCUS | ¿Ha hablado con profesional? | 1=Sí, 2=No |

---

## SECCIÓN 23: CUIDADORES (170-178)

| # | Variable | Descripción |
|---|----------|-------------|
| 170 | **CAREGIV1** | ¿Proporciona cuidado regular a alguien? |
| 171 | CRGVREL4 | Relación con la persona cuidada |
| 172 | CRGVLNG1 | ¿Por cuánto tiempo ha cuidado? |
| 173 | CRGVHRS1 | Horas de cuidado por semana |
| 174 | CRGVPRB3 | Principal problema de salud de la persona |
| 175 | CRGVALZD | ¿La persona tiene Alzheimer/demencia? 🆕 |
| 176 | CRGVPER1 | ¿Ayuda con cuidado personal? |
| 177 | CRGVHOU1 | ¿Ayuda con tareas del hogar? |
| 178 | CRGVEXPT | ¿Espera ser cuidador en próximos 2 años? |

---

## SECCIÓN 24: ACEs - EXPERIENCIAS ADVERSAS EN LA INFANCIA (179-191) ⭐

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 179 | ACEDEPRS | ¿Vivió con alguien deprimido/con enfermedad mental? | 1=Sí, 2=No |
| 180 | ACEDRINK | ¿Vivió con alguien alcohólico? | 1=Sí, 2=No |
| 181 | ACEDRUGS | ¿Vivió con alguien que usaba drogas? | 1=Sí, 2=No |
| 182 | ACEPRISN | ¿Familiar estuvo en prisión? | 1=Sí, 2=No |
| 183 | ACEDIVRC | ¿Padres separados/divorciados? | 1=Sí, 2=No |
| 184 | ACEPUNCH | ¿Vio violencia doméstica? | 1=Sí, 2=No |
| 185 | ACEHURT1 | ¿Fue golpeado/lastimado físicamente? | 1=Sí, 2=No |
| 186 | ACESWEAR | ¿Fue insultado/humillado? | 1=Sí, 2=No |
| 187 | ACETOUCH | ¿Fue tocado sexualmente? | 1=Sí, 2=No |
| 188 | ACETTHEM | ¿Le hicieron tocar sexualmente a alguien? | 1=Sí, 2=No |
| 189 | ACEHVSEX | ¿Fue forzado a tener sexo? | 1=Sí, 2=No |
| 190 | ACEADSAF | ¿Se sintió seguro con adultos? 🆕 | 1=Sí, 2=No |
| 191 | ACEADNED | ¿Adultos cubrieron necesidades básicas? 🆕 | 1=Sí, 2=No |

---

## SECCIÓN 25: BIENESTAR SOCIAL Y DETERMINANTES (192-201) 🆕

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 192 | **LSATISFY** | Satisfacción con la vida | 1=Muy satisfecho, 2=Satisfecho, 3=Insatisfecho, 4=Muy insatisfecho |
| 193 | **EMTSUPRT** | ¿Recibe apoyo emocional que necesita? | 1=Siempre, 2=Usualmente, 3=A veces, 4=Rara vez, 5=Nunca |
| 194 | **SDHISOLT** | **¿Con qué frecuencia se siente aislado?** 🆕 | 1=Siempre a 5=Nunca |
| 195 | SDHEMPLY | ¿Perdió empleo en últimos 12 meses? 🆕 |
| 196 | FOODSTMP | ¿Recibe cupones de alimentos (SNAP)? |
| 197 | SDHFOOD1 | ¿Preocupación por falta de comida? 🆕 |
| 198 | SDHBILLS | ¿Dificultad para pagar cuentas? 🆕 |
| 199 | SDHUTILS | ¿Servicios cortados por falta de pago? 🆕 |
| 200 | SDHTRNSP | ¿Falta de transporte afecta citas médicas? 🆕 |
| 201 | SDHSTRE1 | Nivel de estrés en la vida 🆕 |

---

## SECCIÓN 26: MARIHUANA (202-208) 🆕

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 202 | **MARIJAN1** | **¿Ha usado marihuana alguna vez?** | **1=Sí, 2=No** |
| 203 | MARJSMOK | ¿La fumó? | 1=Sí, 2=No |
| 204 | MARJEAT | ¿La comió/bebió? | 1=Sí, 2=No |
| 205 | MARJVAPE | ¿La vaporizó? | 1=Sí, 2=No |
| 206 | MARJDAB | ¿Usó dabbing? | 1=Sí, 2=No |
| 207 | MARJOTHR | ¿Otra forma de uso? | 1=Sí, 2=No |
| 208 | **USEMRJN4** | **Frecuencia de uso de marihuana (30 días)** | Días |

---

## SECCIÓN 27: TABACO EXTENDIDO (209-213)

| # | Variable | Descripción |
|---|----------|-------------|
| 209 | LASTSMK2 | ¿Hace cuánto dejó de fumar? |
| 210 | STOPSMK2 | ¿Intentó dejar de fumar? |
| 211 | MENTCIGS | ¿Fuma cigarrillos mentolados? 🆕 |
| 212 | MENTECIG | ¿Usa e-cigarrillos mentolados? 🆕 |
| 213 | HEATTBCO | ¿Usa productos de tabaco calentado? 🆕 |

---

## SECCIÓN 28: ALCOHOL SCREENING - ASBI (214-218) 🆕

| # | Variable | Descripción |
|---|----------|-------------|
| 214 | ASBIALCH | ¿Médico preguntó sobre alcohol? |
| 215 | ASBIDRNK | ¿Médico preguntó cantidad? |
| 216 | ASBIBING | ¿Médico preguntó sobre binge drinking? |
| 217 | ASBIADVC | ¿Médico aconsejó reducir? |
| 218 | ASBIRDUC | ¿Ha reducido consumo? |

---

## SECCIÓN 29: ARMAS DE FUEGO (219-221) 🆕

| # | Variable | Descripción |
|---|----------|-------------|
| 219 | FIREARM5 | ¿Hay armas de fuego en el hogar? |
| 220 | GUNLOAD | ¿Hay armas cargadas? |
| 221 | LOADULK2 | ¿Armas cargadas están bajo llave? |

---

## SECCIÓN 30: SALUD INFANTIL Y GÉNERO (222-231)

| # | Variable | Descripción |
|---|----------|-------------|
| 222 | RCSGEND1 | Género del niño seleccionado |
| 223 | RCSXBRTH | Sexo al nacer del niño |
| 224 | RCSRLTN2 | Relación con el niño |
| 225 | CASTHDX2 | ¿Niño tiene asma? |
| 226 | CASTHNO2 | ¿Niño todavía tiene asma? |
| 227 | **BIRTHSEX** | **Sexo al nacer del respondiente** 🆕 |
| 228 | SOMALE | Orientación sexual - atracción a hombres 🆕 |
| 229 | SOFEMALE | Orientación sexual - atracción a mujeres 🆕 |
| 230 | **TRNSGNDR** | **¿Se identifica como transgénero?** 🆕 |
| 231 | HADSEX | ¿Ha tenido relaciones sexuales? |

---

## SECCIÓN 31: PLANIFICACIÓN FAMILIAR (232-237)

| # | Variable | Descripción |
|---|----------|-------------|
| 232 | PFPPRVN4 | ¿Usa método anticonceptivo? |
| 233 | TYPCNTR9 | Tipo de anticonceptivo |
| 234 | BRTHCNT4 | ¿Anticonceptivo para prevenir embarazo? |
| 235 | WHEREGET | ¿Dónde obtiene anticonceptivo? |
| 236 | NOBCUSE8 | Razón para no usar anticonceptivo |
| 237 | BCPREFER | Método anticonceptivo preferido |

---

## SECCIÓN 32: REACCIONES/DISCRIMINACIÓN (238-243)

| # | Variable | Descripción |
|---|----------|-------------|
| 238 | RRCLASS3 | ¿Tratado peor por su raza? |
| 239 | RRCOGNT2 | ¿Tratado como menos inteligente? |
| 240 | RRTREAT | ¿Tratado con menos respeto? 🆕 |
| 241 | RRATWRK2 | ¿Discriminación en el trabajo? |
| 242 | RRHCARE4 | ¿Discriminación en atención médica? |
| 243 | RRPHYSM2 | ¿Sentido amenazado físicamente? |

---

## SECCIÓN 33: ADMINISTRACIÓN Y PESOS (244-262)

| # | Variable | Descripción |
|---|----------|-------------|
| 244 | QSTVER | Versión del cuestionario |
| 245 | QSTLANG | Idioma del cuestionario (1=Inglés, 2=Español) |
| 246 | _METSTAT | Área metropolitana (1=Sí, 2=No) |
| 247 | _URBSTAT | Urbano/Rural |
| 248 | MSCODE | Código metropolitano |
| 249 | _STSTR | Estrato de muestreo |
| 250 | _STRWT | Peso del estrato |
| 251 | _RAWRAKE | Peso bruto con raking |
| 252 | _WT2RAKE | Peso ajustado con raking |
| 253-262 | _IMPRACE - _LLCPWT | Variables imputadas y pesos finales |

---

## SECCIÓN 34: VARIABLES CALCULADAS (263-326) ⭐

### Salud (263-272)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 263 | **_RFHLTH** | **Buena salud (calculada)** | **1=Buena+, 2=Regular/Mala** |
| 264 | _PHYS14D | 14+ días mala salud física | 1=Sí, 2=No |
| 265 | _MENT14D | 14+ días mala salud mental | 1=Sí, 2=No |
| 266 | _HLTHPLN | Tiene plan de salud | 1=Sí, 2=No |
| 267 | _HCVU652 | Sin cobertura (<65 años) | 1=Sin, 2=Con |
| 268 | **_TOTINDA** | **Actividad física** | **1=Activo, 2=Inactivo** |
| 269-271 | _EXTETH3 - _DENVST3 | Variables dentales calculadas |
| 272 | _MICHD | Enfermedad coronaria o infarto | 1=Sí, 2=No |

### Condiciones Crónicas (273-276)
| # | Variable | Descripción |
|---|----------|-------------|
| 273 | _LTASTH1 | Asma alguna vez |
| 274 | _CASTHM1 | Asma actual |
| 275 | _ASTHMS1 | Estado de asma (actual/anterior/nunca) |
| 276 | _DRDXAR2 | Artritis diagnosticada |

### Raza/Etnicidad (277-283)
| # | Variable | Descripción |
|---|----------|-------------|
| 277-283 | _PRACE2 - _RACEPR1 | Clasificaciones de raza |

### Demografía (284-297)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 284 | **_SEX** | Sexo calculado | 1=Masculino, 2=Femenino |
| 285 | **_AGEG5YR** | Grupos de edad (5 años) | 1=18-24, 2=25-29, ... 13=80+ |
| 286 | **_AGE65YR** | 65+ años | 1=18-64, 2=65+ |
| 287 | **_AGE80** | Edad (máximo 80) | 18-80 |
| 288 | **_AGE_G** | Grupos de edad (6 niveles) | 1=18-24 a 6=65+ |
| 289 | HTIN4 | Altura en pulgadas |
| 290 | HTM4 | Altura en metros (×100) |
| 291 | WTKG3 | Peso en kg (×100) |
| 292 | **_BMI5** | **IMC (×100)** |
| 293 | **_BMI5CAT** | **Categoría IMC** | **1=Bajo, 2=Normal, 3=Sobrepeso, 4=Obeso** |
| 294 | **_RFBMI5** | **Sobrepeso/Obeso** | **1=No, 2=Sí** |
| 295 | _CHLDCNT | Conteo de niños |
| 296 | **_EDUCAG** | **Nivel educativo (4 niveles)** | **1=Sin sec, 2=Sec, 3=Algo univ, 4=Univ** |
| 297 | **_INCOMG1** | **Ingreso (6 niveles)** | **1=<$15K a 6=>$50K** |

### Detección de Cáncer (298-309)
| # | Variable | Descripción |
|---|----------|-------------|
| 298-299 | _RFMAM22 - _MAM5023 | Mamografía calculada |
| 300-309 | _HADCOLN - _CRCREC2 | Detección colorrectal calculada |

### Tabaco (310-318)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 310 | **_SMOKER3** | **Estado de fumador** | **1=Diario, 2=Algunos días, 3=Ex-fumador, 4=Nunca** |
| 311 | **_RFSMOK3** | **Fumador actual** | **1=No, 2=Sí** |
| 312 | _CURECI2 | Usa e-cigarrillos actualmente 🆕 |
| 313 | _YRSSMOK | Años fumando |
| 314 | _PACKDAY | Paquetes por día |
| 315 | _PACKYRS | Paquetes-año |
| 316 | _YRSQUIT | Años desde que dejó |
| 317 | _SMOKGRP | Grupo de fumador |
| 318 | _LCSREC | Elegible para screening de pulmón |

### Alcohol (319-323)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 319 | DRNKANY6 | Bebió en últimos 30 días | 1=Sí, 2=No |
| 320 | DROCDY4_ | Ocasiones de consumo |
| 321 | **_RFBING6** | **Bebedor excesivo (binge)** | **1=No, 2=Sí** |
| 322 | _DRNKWK2 | Bebidas por semana |
| 323 | **_RFDRHV8** | **Bebedor de alto riesgo** | **1=No, 2=Sí** |

### Inmunizaciones y VIH (324-326)
| # | Variable | Descripción |
|---|----------|-------------|
| 324 | _FLSHOT7 | Adultos 65+ con vacuna gripe |
| 325 | _PNEUMO3 | Adultos 65+ con vacuna neumonía |
| 326 | _AIDTST4 | Prueba de VIH alguna vez |

---

# COMPARACIÓN 2011 vs 2022

## Variables NUEVAS en 2022 (no existían en 2011):

| Categoría | Variables Nuevas |
|-----------|-----------------|
| **COVID-19** | COVIDPOS, COVIDSMP, COVIDPRM, COVIDVA1, COVIDNU1 |
| **E-cigarrillos** | ECIGNOW2, _CURECI2 |
| **Marihuana** | MARIJAN1, MARJSMOK, MARJEAT, MARJVAPE, USEMRJN4 |
| **Determinantes Sociales** | SDHISOLT, SDHEMPLY, SDHFOOD1, SDHBILLS, SDHTRNSP |
| **Armas de Fuego** | FIREARM5, GUNLOAD, LOADULK2 |
| **Género/Sexualidad** | BIRTHSEX, SOMALE, SOFEMALE, TRNSGNDR |
| **Fatiga Crónica** | TOLDCFS, HAVECFS, WORKCFS |
| **Salud Oral** | LASTDEN4, RMVTETH4 |
| **Sordera** | DEAF |

## Variables COMPARABLES entre ambos años:

| Variable 2011 | Variable 2022 | Descripción |
|---------------|---------------|-------------|
| GENHLTH | GENHLTH | Salud general |
| PHYSHLTH | PHYSHLTH | Días mala salud física |
| MENTHLTH | MENTHLTH | Días mala salud mental |
| SLEPTIME | SLEPTIM1 | Horas de sueño |
| ADDEPEV2 | ADDEPEV3 | Depresión diagnosticada |
| DIABETE3 | DIABETE4 | Diabetes |
| SMOKE100/SMOKDAY2 | SMOKE100/SMOKDAY2 | Tabaquismo |
| ALCDAY5 | ALCDAY4 | Consumo de alcohol |
| _SMOKER3 | _SMOKER3 | Estado de fumador (calculada) |
| _RFSMOK3 | _RFSMOK3 | Fumador actual (calculada) |
| _BMI5CAT | _BMI5CAT | Categoría IMC |
| _RFBMI5 | _RFBMI5 | Sobrepeso/obeso |
| _TOTINDA | _TOTINDA | Actividad física |
| _EDUCAG | _EDUCAG | Nivel educativo |
| _AGE_G | _AGE_G | Grupos de edad |
| SEX | _SEX | Sexo |

---

# RESUMEN FINAL

| Característica | 2011 | 2022 |
|---------------|------|------|
| **Total columnas** | 454 | 326 |
| **Registros** | 506,467 | 445,132 |
| **Variable sueño** | SLEPTIME (col 146) | SLEPTIM1 (col 42) |
| **Depresión** | ADDEPEV2 | ADDEPEV3 |
| **Diabetes** | DIABETE3 | DIABETE4 |
| **COVID-19** | ❌ No existe | ✅ COVIDPOS, COVIDVA1 |
| **E-cigarrillos** | ❌ No existe | ✅ ECIGNOW2 |
| **Marihuana** | ❌ No existe | ✅ MARIJAN1 |

---

*Total: 326 variables en BRFSS 2022*
*Documento para proyecto de Estadística - Universidad de La Habana, MATCOM*
