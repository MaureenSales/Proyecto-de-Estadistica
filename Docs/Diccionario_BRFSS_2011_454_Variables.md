# Diccionario de Variables BRFSS 2011
## Total: 454 columnas

---

# RESUMEN POR CATEGORÍAS

| Categoría | Cantidad | Rango de columnas |
|-----------|----------|-------------------|
| Identificación y Muestreo | 24 | 1-24 |
| Estado de Salud General | 4 | 25-28 |
| Acceso a Servicios de Salud | 4 | 29-32 |
| Condiciones Crónicas | 18 | 33-50 |
| Tabaco | 5 | 51-55 |
| Demografía | 22 | 56-77 |
| Nutrición | 6 | 78-83 |
| Actividad Física | 8 | 84-91 |
| Discapacidad y Artritis | 6 | 92-97 |
| Inmunizaciones y Prevención | 5 | 98-102 |
| Alcohol | 4 | 103-106 |
| VIH | 3 | 107-109 |
| Diabetes (módulo) | 12 | 110-121 |
| Calidad de Vida | 4 | 122-125 |
| Módulos Opcionales | ~200 | 126-327 |
| Pesos y Variables Calculadas | ~127 | 328-454 |

---

# DETALLE DE CADA VARIABLE

## SECCIÓN 1: IDENTIFICACIÓN Y MUESTREO (1-24)

| # | Variable | Descripción |
|---|----------|-------------|
| 1 | _STATE | Código FIPS del estado (1-72) |
| 2 | _GEOSTR | Código de estrato geográfico |
| 3 | _DENSTR2 | Código de densidad del hogar (1=Listed, 2=Unlisted, 9=N/A) |
| 4 | PRECALL | Código de estado de pre-llamada |
| 5 | REPNUM | Número de replicación |
| 6 | REPDEPTH | Profundidad de replicación |
| 7 | FMONTH | Mes del archivo (1-12) |
| 8 | IDATE | Fecha de entrevista (MMDDYYYY) |
| 9 | IMONTH | Mes de entrevista (01-12) |
| 10 | IDAY | Día de entrevista (01-31) |
| 11 | IYEAR | Año de entrevista (2011) |
| 12 | INTVID | ID del entrevistador |
| 13 | DISPCODE | Código de disposición final (110=Completa) |
| 14 | SEQNO | Número de secuencia anual (único por estado/año) |
| 15 | _PSU | Unidad de muestreo primaria |
| 16 | NATTMPTS | Número de intentos de contacto |
| 17 | NRECSEL | Número de adultos seleccionados |
| 18 | NRECSTR | Número de registros en estrato |
| 19 | CTELENUM | ¿Número telefónico correcto? (1=Sí, 2=No) |
| 20 | CELLFON | ¿Es teléfono celular? (1=Sí, 2=No) |
| 21 | PVTRESID | ¿Residencia privada? (1=Sí, 2=No) |
| 22 | NUMADULT | Número de adultos en el hogar |
| 23 | NUMMEN | Número de hombres adultos |
| 24 | NUMWOMEN | Número de mujeres adultas |

---

## SECCIÓN 2: ESTADO DE SALUD GENERAL (25-28)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 25 | GENHLTH | Salud general autopercibida | 1=Excelente, 2=Muy buena, 3=Buena, 4=Regular, 5=Mala, 7=NS, 9=Rechazó |
| 26 | PHYSHLTH | Días de mala salud física (últimos 30 días) | 1-30=Días, 88=Ninguno, 77=NS, 99=Rechazó |
| 27 | MENTHLTH | Días de mala salud mental (últimos 30 días) | 1-30=Días, 88=Ninguno, 77=NS, 99=Rechazó |
| 28 | POORHLTH | Días con actividad limitada por mala salud | 1-30=Días, 88=Ninguno, 77=NS, 99=Rechazó |

---

## SECCIÓN 3: ACCESO A SERVICIOS DE SALUD (29-32)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 29 | HLTHPLN1 | ¿Tiene cobertura de salud? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 30 | PERSDOC2 | ¿Tiene médico personal? | 1=Sí uno, 2=Más de uno, 3=No, 7=NS, 9=Rechazó |
| 31 | MEDCOST | ¿No pudo ver médico por costo? (12 meses) | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 32 | CHECKUP1 | Tiempo desde último chequeo | 1=<1 año, 2=1-2 años, 3=2-5 años, 4=>5 años, 8=Nunca, 7=NS, 9=Rechazó |

---

## SECCIÓN 4: CONDICIONES CRÓNICAS (33-50)

### Cardiovascular (33-40)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 33 | BPHIGH4 | ¿Le dijeron que tiene presión alta? | 1=Sí, 2=Sí embarazo, 3=No, 4=Borderline, 7=NS, 9=Rechazó |
| 34 | BPMEDS | ¿Toma medicamentos para presión? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 35 | BLOODCHO | ¿Le han revisado colesterol? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 36 | CHOLCHK | ¿Cuándo fue el último chequeo de colesterol? | 1=<1 año, 2=1-2 años, 3=2-5 años, 4=>5 años, 8=Nunca, 7=NS, 9=Rechazó |
| 37 | TOLDHI2 | ¿Le dijeron que tiene colesterol alto? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 38 | CVDINFR4 | ¿Le dijeron que tuvo infarto? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 39 | CVDCRHD4 | ¿Le dijeron que tiene enfermedad coronaria? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 40 | CVDSTRK3 | ¿Le dijeron que tuvo derrame cerebral? | 1=Sí, 2=No, 7=NS, 9=Rechazó |

### Respiratorio y Otros (41-50)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 41 | ASTHMA3 | ¿Le dijeron que tiene asma? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 42 | ASTHNOW | ¿Todavía tiene asma? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 43 | CHCSCNCR | ¿Le dijeron que tiene cáncer de piel? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 44 | CHCOCNCR | ¿Le dijeron que tiene otro tipo de cáncer? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 45 | CHCCOPD | ¿Le dijeron que tiene EPOC/enfisema/bronquitis? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 46 | HAVARTH3 | ¿Le dijeron que tiene artritis? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 47 | ADDEPEV2 | ¿Le dijeron que tiene depresión? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 48 | CHCKIDNY | ¿Le dijeron que tiene enfermedad renal? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 49 | CHCVISON | ¿Tiene problemas de visión? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 50 | DIABETE3 | ¿Le dijeron que tiene diabetes? | 1=Sí, 2=Sí embarazo, 3=No, 4=Pre-diabetes, 7=NS, 9=Rechazó |

---

## SECCIÓN 5: TABACO (51-55)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 51 | SMOKE100 | ¿Ha fumado 100+ cigarrillos en su vida? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 52 | SMOKDAY2 | ¿Fuma actualmente? | 1=Todos los días, 2=Algunos días, 3=Nunca, 7=NS, 9=Rechazó |
| 53 | STOPSMK2 | ¿Intentó dejar de fumar (12 meses)? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 54 | LASTSMK2 | ¿Hace cuánto dejó de fumar? | 1=<1 mes, 2=1-3 meses, 3=3-6 meses, 4=6-12 meses, 5=1-5 años, 6=5-10 años, 7=10+ años, 8=Nunca fumó regularmente |
| 55 | USENOW3 | ¿Usa tabaco sin humo actualmente? | 1=Todos los días, 2=Algunos días, 3=Nunca, 7=NS, 9=Rechazó |

---

## SECCIÓN 6: DEMOGRAFÍA (56-77)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 56 | AGE | Edad reportada | 18-99 años, 7=NS, 9=Rechazó |
| 57 | HISPANC2 | ¿Es hispano/latino? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 58 | MRACE | Raza (múltiple) | Código de raza múltiple |
| 59 | ORACE2 | Otra raza | Código de otra raza |
| 60 | VETERAN3 | ¿Es veterano? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 61 | MARITAL | Estado civil | 1=Casado, 2=Divorciado, 3=Viudo, 4=Separado, 5=Nunca casado, 6=Pareja, 9=Rechazó |
| 62 | CHILDREN | Niños <18 en el hogar | 1-87=Número, 88=Ninguno, 99=Rechazó |
| 63 | EDUCA | Nivel educativo | 1=Nunca/Kinder, 2=Elemental, 3=Algo secundaria, 4=Graduado secundaria, 5=Algo universidad, 6=Graduado universidad, 9=Rechazó |
| 64 | EMPLOY | Situación laboral | 1=Empleado, 2=Autoempleado, 3=Desempleado >1año, 4=Desempleado <1año, 5=Hogar, 6=Estudiante, 7=Retirado, 8=Incapacitado, 9=Rechazó |
| 65 | INCOME2 | Ingreso anual del hogar | 1=<$10K, 2=$10-15K, 3=$15-20K, 4=$20-25K, 5=$25-35K, 6=$35-50K, 7=$50-75K, 8=>$75K, 77=NS, 99=Rechazó |
| 66 | WEIGHT2 | Peso (libras o kg con 9 al inicio) | Peso numérico |
| 67 | HEIGHT3 | Altura (pies/pulgadas o metros con 9) | Altura numérica |
| 68 | CTYCODE1 | Código del condado | Código FIPS |
| 69 | NUMHHOL2 | ¿Más de un teléfono en el hogar? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 70 | NUMPHON2 | Número de teléfonos residenciales | 1-6=Número, 7=NS, 9=Rechazó |
| 71 | CPDEMO1 | ¿Tiene celular personal? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 72 | CPDEMO2 | Pregunta demo celular 2 | Variable demográfica |
| 73 | CPDEMO3 | Pregunta demo celular 3 | Variable demográfica |
| 74 | CPDEMO4 | Pregunta demo celular 4 | Variable demográfica |
| 75 | RENTHOM1 | ¿Alquila o es propietario? | 1=Propietario, 2=Alquila, 3=Otro, 7=NS, 9=Rechazó |
| 76 | SEX | Sexo | 1=Masculino, 2=Femenino |
| 77 | PREGNANT | ¿Está embarazada? | 1=Sí, 2=No, 7=NS, 9=Rechazó |

---

## SECCIÓN 7: NUTRICIÓN (78-83)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 78 | FRUITJU1 | Veces que tomó jugo de fruta 100% | Formato: 1XX=por día, 2XX=por semana, 3XX=por mes, 300=Nunca |
| 79 | FRUIT1 | Veces que comió fruta | Mismo formato |
| 80 | FVBEANS | Veces que comió frijoles/legumbres | Mismo formato |
| 81 | FVGREEN | Veces que comió vegetales verdes oscuros | Mismo formato |
| 82 | FVORANG | Veces que comió vegetales anaranjados | Mismo formato |
| 83 | VEGETAB1 | Veces que comió otros vegetales | Mismo formato |

---

## SECCIÓN 8: ACTIVIDAD FÍSICA (84-91)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 84 | EXERANY2 | ¿Hizo ejercicio en el último mes? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 85 | EXRACT01 | Tipo de actividad física principal | Código de actividad (ver manual) |
| 86 | EXEROFT1 | Frecuencia de actividad 1 | 1XX=por semana, 2XX=por mes |
| 87 | EXERHMM1 | Duración de actividad 1 (minutos) | Minutos por sesión |
| 88 | EXRACT02 | Tipo de segunda actividad física | Código de actividad |
| 89 | EXEROFT2 | Frecuencia de actividad 2 | 1XX=por semana, 2XX=por mes |
| 90 | EXERHMM2 | Duración de actividad 2 (minutos) | Minutos por sesión |
| 91 | STRENGTH | Frecuencia de ejercicios de fuerza | 1XX=por semana, 2XX=por mes, 888=Nunca |

---

## SECCIÓN 9: DISCAPACIDAD Y ARTRITIS (92-97)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 92 | QLACTLM2 | ¿Limitado en actividades? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 93 | USEEQUIP | ¿Usa equipo especial? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 94 | LMTJOIN3 | ¿Limitado por artritis? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 95 | ARTHDIS2 | ¿Artritis afecta trabajo? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 96 | ARTHSOCL | ¿Artritis interfiere con actividades sociales? | 1=Mucho, 2=Algo, 3=Poco, 4=Nada, 7=NS, 9=Rechazó |
| 97 | JOINPAIN | Nivel de dolor articular (0-10) | 0-10 escala |

---

## SECCIÓN 10: INMUNIZACIONES (98-102)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 98 | SEATBELT | ¿Con qué frecuencia usa cinturón? | 1=Siempre, 2=Casi siempre, 3=A veces, 4=Rara vez, 5=Nunca, 7=NS, 8=Nunca viaja, 9=Rechazó |
| 99 | FLUSHOT5 | ¿Vacuna de gripe en últimos 12 meses? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 100 | FLSHTMY2 | Mes/año de última vacuna de gripe | MMYYYY |
| 101 | IMFVPLAC | Lugar donde recibió vacuna | 1=Consultorio, 2=Centro salud, 3=Hospital, etc. |
| 102 | PNEUVAC3 | ¿Ha recibido vacuna de neumonía? | 1=Sí, 2=No, 7=NS, 9=Rechazó |

---

## SECCIÓN 11: ALCOHOL (103-106)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 103 | ALCDAY5 | Días con alcohol en últimos 30 | 1XX=días/semana, 2XX=días/mes, 888=Ninguno |
| 104 | AVEDRNK2 | Promedio de bebidas por ocasión | 1-76=Número, 77=NS, 99=Rechazó |
| 105 | DRNK3GE5 | Veces con 5+ bebidas (30 días) | 1-76=Veces, 88=Ninguna, 77=NS, 99=Rechazó |
| 106 | MAXDRNKS | Máximo bebidas en una ocasión | 1-76=Número, 77=NS, 99=Rechazó |

---

## SECCIÓN 12: VIH (107-109)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 107 | HIVTST6 | ¿Se ha hecho prueba de VIH? | 1=Sí, 2=No, 7=NS, 9=Rechazó |
| 108 | HIVTSTD3 | Mes/año de última prueba VIH | MMYYYY |
| 109 | HIVRISK3 | Comportamientos de riesgo VIH | 1=Sí, 2=No, 7=NS, 9=Rechazó |

---

## SECCIÓN 13: DIABETES - MÓDULO (110-121)

| # | Variable | Descripción |
|---|----------|-------------|
| 110 | PDIABTST | ¿Prueba de diabetes en últimos 3 años? |
| 111 | PREDIAB1 | ¿Le dijeron que tiene pre-diabetes? |
| 112 | DIABAGE2 | Edad cuando le diagnosticaron diabetes |
| 113 | INSULIN | ¿Usa insulina actualmente? |
| 114 | BLDSUGAR | Frecuencia de revisión de glucosa |
| 115 | FEETCHK2 | Frecuencia de revisión de pies (personal) |
| 116 | DOCTDIAB | Visitas al médico por diabetes (12 meses) |
| 117 | CHKHEMO3 | Veces que le revisaron A1C |
| 118 | FEETCHK | Revisión de pies por profesional (12 meses) |
| 119 | EYEEXAM | Último examen de ojos dilatados |
| 120 | DIABEYE | ¿Diabetes afectó sus ojos? |
| 121 | DIABEDU | ¿Tomó curso de manejo de diabetes? |

---

## SECCIÓN 14: CALIDAD DE VIDA (122-125)

| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 122 | PAINACT2 | Días que el dolor dificultó actividades | 0-30 días |
| 123 | QLMENTL2 | Días sintiéndose triste/deprimido | 0-30 días |
| 124 | QLSTRES2 | Días sintiéndose preocupado/ansioso | 0-30 días |
| 125 | QLHLTH2 | Días sintiéndose saludable/energético | 0-30 días |

---

## SECCIÓN 15: MÓDULOS OPCIONALES (126-327)

### Bebidas Azucaradas (126-128)
| # | Variable | Descripción |
|---|----------|-------------|
| 126 | SSBSUGAR | Consumo de bebidas azucaradas |
| 127 | SSBFRUIT | Consumo de bebidas de fruta |
| 128 | SSBCALRI | Consumo de bebidas con calorías |

### Planificación Familiar (129-135)
| # | Variable | Descripción |
|---|----------|-------------|
| 129 | PFPPREPR | Preparación para embarazo |
| 130 | PFPPRGNT | Estado de embarazo |
| 131 | PFPPRVNT | Prevención de embarazo |
| 132 | TYPCNTR6 | Tipo de anticonceptivo |
| 133 | NOBCUSE4 | Razón para no usar anticonceptivo |
| 134 | FPCHLDF2 | Planificación de hijos futuros |
| 135 | PFPVITMN | Uso de vitaminas prenatales |

### Visión (136-144)
| # | Variable | Descripción |
|---|----------|-------------|
| 136 | VIDFCLT3 | Dificultad para ver de lejos |
| 137 | VIREDIF3 | Dificultad para leer |
| 138 | VIPRFVS3 | Último examen de ojos |
| 139 | VINOCRE3 | Razón para no visitar oftalmólogo |
| 140 | VIEYEXM3 | Examen de ojos dilatados |
| 141 | VIINSUR3 | Seguro para cuidado de ojos |
| 142 | VICTRCT3 | ¿Tiene cataratas? |
| 143 | VIGLUMA3 | ¿Tiene glaucoma? |
| 144 | VIMACDG3 | ¿Tiene degeneración macular? |

### **SUEÑO (145-149)** ⭐ IMPORTANTE PARA TU PROYECTO
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 145 | QLREST2 | Días sintiéndose descansado | 0-30 días |
| 146 | **SLEPTIME** | **Horas de sueño promedio en 24h** | **1-24 horas** |
| 147 | SLEPSNOR | ¿Ronca mientras duerme? | 1=Sí, 2=No |
| 148 | SLEPDAY | ¿Se queda dormido durante el día? | 1-30 días |
| 149 | SLEPDRIV | ¿Se quedó dormido manejando? | 1=Sí, 2=No |

### Rehabilitación Cardíaca (150-154)
| # | Variable | Descripción |
|---|----------|-------------|
| 150 | WRKHCF1 | ¿Trabaja en centro de salud? |
| 151 | DIRCONT1 | Contacto directo con pacientes |
| 152 | DRHPAD1 | Promoción de rehabilitación |
| 153 | HAREHAB1 | ¿Ha tenido rehabilitación cardíaca? |
| 154 | STREHAB1 | ¿Completó programa de rehabilitación? |

### Aspirina Cardiovascular (155-156)
| # | Variable | Descripción |
|---|----------|-------------|
| 155 | CVDASPRN | ¿Toma aspirina para corazón? |
| 156 | ASPUNSAF | ¿Considera insegura la aspirina? |

### Manejo de Presión Arterial (157-166)
| # | Variable | Descripción |
|---|----------|-------------|
| 157 | BPEATHBT | Consejo: comer más frutas/verduras |
| 158 | BPSALT | Consejo: reducir sal |
| 159 | BPALCHOL | Consejo: reducir alcohol |
| 160 | BPEXER | Consejo: hacer ejercicio |
| 161-166 | BPEATADV - BPHI2MR | Otros consejos médicos |

### Síntomas de Ataque Cardíaco y Derrame (167-179)
| # | Variable | Descripción |
|---|----------|-------------|
| 167-172 | HASYMP1-6 | Síntomas de ataque cardíaco |
| 173-178 | STRSYMP1-6 | Síntomas de derrame cerebral |
| 179 | FIRSTAID | ¿Sabe primeros auxilios? |

### Detección de Cáncer - Mujeres (180-186)
| # | Variable | Descripción |
|---|----------|-------------|
| 180 | HADMAM | ¿Ha tenido mamografía? |
| 181 | HOWLONG | ¿Hace cuánto fue la mamografía? |
| 182 | PROFEXAM | ¿Ha tenido examen de seno profesional? |
| 183 | LENGEXAM | ¿Hace cuánto fue el examen? |
| 184 | HADPAP2 | ¿Ha tenido Papanicolau? |
| 185 | LASTPAP2 | ¿Hace cuánto fue el Pap? |
| 186 | HADHYST2 | ¿Ha tenido histerectomía? |

### Detección de Cáncer - Hombres (187-194)
| # | Variable | Descripción |
|---|----------|-------------|
| 187 | PCPSAREC | Recomendación de PSA |
| 188 | PSATEST1 | ¿Se ha hecho prueba PSA? |
| 189 | PSATIME | ¿Hace cuánto fue la prueba? |
| 190-194 | PCPSARSN - PROSTATE | Decisiones sobre PSA y próstata |

### Detección Colorrectal (195-199)
| # | Variable | Descripción |
|---|----------|-------------|
| 195 | BLDSTOOL | ¿Prueba de sangre oculta? |
| 196 | LSTBLDS3 | ¿Hace cuánto fue la prueba? |
| 197 | HADSIGM3 | ¿Ha tenido sigmoidoscopia/colonoscopia? |
| 198 | HADSGCO1 | Tipo de examen |
| 199 | LASTSIG3 | ¿Hace cuánto fue el examen? |

### Cesación de Tabaco (200-207)
| # | Variable | Descripción |
|---|----------|-------------|
| 200 | SMCQUITL | Línea de ayuda para dejar de fumar |
| 201-207 | SMCTRYQT - SMCPLANQ | Métodos para dejar de fumar |

### Humo de Segunda Mano (208-214)
| # | Variable | Descripción |
|---|----------|-------------|
| 208 | SHSNWRK1 | Exposición en trabajo |
| 209 | SHSNHOM1 | Exposición en hogar |
| 210-214 | SHSRIDEV - SHSALOW1 | Otros lugares de exposición |

### Asma - Módulo Extendido (215-224)
| # | Variable | Descripción |
|---|----------|-------------|
| 215 | ASTHMAGE | Edad de diagnóstico de asma |
| 216 | ASATTACK | Ataques de asma (12 meses) |
| 217-224 | ASERVIST - ASINHALR | Visitas, síntomas, medicamentos |

### Artritis - Módulo Extendido (225-228)
| # | Variable | Descripción |
|---|----------|-------------|
| 225 | ARTTODAY | Dolor de artritis hoy |
| 226 | ARTHWGT | Consejo: perder peso |
| 227 | ARTHEXER | Consejo: hacer ejercicio |
| 228 | ARTHEDU | ¿Tomó curso sobre artritis? |

### Vacunas (229-234)
| # | Variable | Descripción |
|---|----------|-------------|
| 229-231 | TNSARCV - TNSASHT1 | Vacuna de tétanos |
| 232-233 | HPVADVC2 - HPVADSHT | Vacuna VPH |
| 234 | SHINGLE1 | Vacuna de herpes zóster |

### EPOC - Módulo (235-239)
| # | Variable | Descripción |
|---|----------|-------------|
| 235 | COPDTEST | ¿Prueba de EPOC? |
| 236 | COPDQOL | Calidad de vida con EPOC |
| 237-239 | COPDDOC - COPDMEDS | Tratamiento de EPOC |

### Preparación para Emergencias (240-250)
| # | Variable | Descripción |
|---|----------|-------------|
| 240 | GPWELPR3 | ¿Tiene pozo de agua? |
| 241-250 | GP3DYWTR - GPNOTEV1 | Preparación para desastres |

### Salud de Veteranos (251-256)
| # | Variable | Descripción |
|---|----------|-------------|
| 251 | VHCOMBAT | ¿Estuvo en combate? |
| 252 | VHDRPTSD | ¿Diagnosticado con PTSD? |
| 253 | VHDRTBI | ¿Lesión cerebral traumática? |
| 254-256 | VHCOUNSL - VHSUICID | Consejería y pensamientos suicidas |

### Reacción/Discriminación (257-262)
| # | Variable | Descripción |
|---|----------|-------------|
| 257-262 | RRCLASS2 - RREMTSM2 | Experiencias de discriminación |

### **Depresión PHQ-8 (263-272)** ⭐ IMPORTANTE
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 263 | ADPLEASR | Poco interés o placer | 1=Nunca, 2=Varios días, 3=Más de mitad, 4=Casi todos |
| 264 | ADDOWN | Sentirse deprimido | Misma escala |
| 265 | ADSLEEP | Problemas de sueño | Misma escala |
| 266 | ADENERGY | Sentirse cansado | Misma escala |
| 267 | ADEAT1 | Poco apetito o comer mucho | Misma escala |
| 268 | ADFAIL | Sentirse fracasado | Misma escala |
| 269 | ADTHINK | Dificultad para concentrarse | Misma escala |
| 270 | ADMOVE | Moverse lento o inquieto | Misma escala |
| 271 | MISTMNT | ¿Recibe tratamiento? | 1=Sí, 2=No |
| 272 | ADANXEV | ¿Ansiedad diagnosticada? | 1=Sí, 2=No |

### Deterioro Cognitivo (273-282)
| # | Variable | Descripción |
|---|----------|-------------|
| 273 | CIMEMLOS | Confusión/pérdida de memoria |
| 274-282 | CINOADLT - CIDIAGAZ | Impacto y diagnóstico |

### Seguridad Alimentaria (283-288)
| # | Variable | Descripción |
|---|----------|-------------|
| 283 | SCNTMONY | ¿Faltó dinero para comida? |
| 284-288 | SCNTMEAL - SCNTLWK1 | Otros indicadores de inseguridad |

### VIH Extendido (289-290)
| # | Variable | Descripción |
|---|----------|-------------|
| 289 | WHRTST9 | Lugar de última prueba VIH |
| 290 | HIVRDTS2 | Prueba rápida de VIH |

### Apoyo Social (291-292)
| # | Variable | Descripción |
|---|----------|-------------|
| 291 | EMTSUPRT | ¿Recibe apoyo emocional que necesita? |
| 292 | LSATISFY | Satisfacción con la vida |

### **Experiencias Adversas en la Infancia - ACEs (293-303)** ⭐
| # | Variable | Descripción |
|---|----------|-------------|
| 293 | ACEDEPRS | ¿Vivió con alguien deprimido? |
| 294 | ACEDRINK | ¿Vivió con alcohólico? |
| 295 | ACEDRUGS | ¿Vivió con usuario de drogas? |
| 296 | ACEPRISN | ¿Familiar en prisión? |
| 297 | ACEDIVRC | ¿Padres separados/divorciados? |
| 298 | ACEPUNCH | ¿Vio violencia doméstica? |
| 299 | ACEHURT | ¿Fue golpeado/lastimado? |
| 300 | ACESWEAR | ¿Fue insultado/humillado? |
| 301 | ACETOUCH | ¿Fue tocado sexualmente? |
| 302 | ACETTHEM | ¿Le hicieron tocar sexualmente? |
| 303 | ACEHVSEX | ¿Fue forzado a tener sexo? |

### Salud Infantil (304-316)
| # | Variable | Descripción |
|---|----------|-------------|
| 304-309 | RCSBIRTH - RCSRLTN2 | Datos del niño seleccionado |
| 310-316 | CASTHDX2 - ADLTCHLD | Salud del niño |

### Celular (317-327)
| # | Variable | Descripción |
|---|----------|-------------|
| 317-327 | CTELNUM1 - MSCODE | Variables de muestra celular |

---

## SECCIÓN 16: PESOS Y VARIABLES CALCULADAS (328-454)

### Pesos de Muestreo (328-362)
| # | Variable | Descripción |
|---|----------|-------------|
| 328 | _STSTR | Estrato de muestreo |
| 329 | _STRWT | Peso del estrato |
| 330 | _RAW | Peso bruto |
| 331 | _WT2 | Peso ajustado |
| 332 | _RAWRAKE | Peso bruto con raking |
| 333 | _WT2RAKE | Peso con raking |
| 334 | _REGION | Región del país |
| 335-337 | _IMPAGE - _IMPNPH | Variables imputadas |
| 338-362 | O_STATE - _LLCPWT | Pesos adicionales y de módulos |

### **Variables Calculadas de Factores de Riesgo (363-373)** ⭐
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 363 | **_RFHLTH** | **Buena salud** | **1=Buena+, 2=Regular/Mala** |
| 364 | _HCVU651 | Sin cobertura (<65 años) | 1=Sin cobertura, 2=Con cobertura |
| 365 | **_RFHYPE5** | **Hipertensión** | **1=No, 2=Sí** |
| 366 | _CHOLCHK | Chequeo de colesterol | 1=Revisado, 2=No |
| 367 | **_RFCHOL** | **Colesterol alto** | **1=No, 2=Sí** |
| 368 | _LTASTH1 | Asma alguna vez | 1=Sí, 2=No |
| 369 | _CASTHM1 | Asma actual | 1=Sí, 2=No |
| 370 | _ASTHMS1 | Estado de asma | 1=Actual, 2=Anterior, 3=Nunca |
| 371 | _DRDXAR1 | Artritis diagnosticada | 1=Sí, 2=No |
| 372 | **_SMOKER3** | **Estado de fumador** | **1=Diario, 2=Algunos días, 3=Ex-fumador, 4=Nunca** |
| 373 | **_RFSMOK3** | **Fumador actual** | **1=No, 2=Sí** |

### Variables de Raza (374-383)
| # | Variable | Descripción |
|---|----------|-------------|
| 374-383 | MRACEORG - _CNRACEC | Clasificaciones de raza/etnicidad |

### **Variables de Edad (384-386)** ⭐
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 384 | **_AGEG5YR** | **Grupos de edad (5 años)** | 1=18-24, 2=25-29, ..., 13=80+ |
| 385 | **_AGE65YR** | **65+ años** | **1=18-64, 2=65+** |
| 386 | **_AGE_G** | **Grupos de edad (6 niveles)** | 1=18-24, 2=25-34, 3=35-44, 4=45-54, 5=55-64, 6=65+ |

### Variables de Peso/Altura/IMC (387-392)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 387 | HTIN4 | Altura en pulgadas | Pulgadas |
| 388 | HTM4 | Altura en metros | Metros ×100 |
| 389 | WTKG3 | Peso en kg | Kg ×100 |
| 390 | **_BMI5** | **IMC** | **IMC ×100** |
| 391 | **_BMI5CAT** | **Categoría IMC** | **1=Bajo peso, 2=Normal, 3=Sobrepeso, 4=Obeso** |
| 392 | **_RFBMI5** | **Sobrepeso/Obeso** | **1=No, 2=Sí** |

### Variables Demográficas Calculadas (393-395)
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 393 | _CHLDCNT | Conteo de niños | Número de niños |
| 394 | **_EDUCAG** | **Nivel educativo (4 niveles)** | **1=Sin secundaria, 2=Secundaria, 3=Algo universidad, 4=Universidad** |
| 395 | **_INCOMG** | **Ingreso (5 niveles)** | **1=<$15K, 2=$15-25K, 3=$25-35K, 4=$35-50K, 5=>$50K** |

### Variables de Nutrición Calculadas (396-411)
| # | Variable | Descripción |
|---|----------|-------------|
| 396-401 | FTJUDA1_ - VEGEDA1_ | Consumo diario de frutas/vegetales |
| 402-403 | _MISFRTN - _MISVEGN | Datos faltantes |
| 404-407 | _FRTRESP - _VEGESUM | Totales de frutas y vegetales |
| 408-411 | _FRT16 - _VEGETEX | Variables calculadas adicionales |

### **Variables de Actividad Física (412-440)** ⭐
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 412 | **_TOTINDA** | **Actividad física en tiempo libre** | **1=Activo, 2=Inactivo** |
| 413-432 | METVAL1_ - PAVIGMN_ | METs, intensidad, duración |
| 433 | **_PACAT** | **Categoría de actividad** | **1=Muy activo, 2=Activo, 3=Insuficiente, 4=Inactivo** |
| 434 | **_PAINDEX** | **Cumple recomendaciones aeróbicas** | **1=Sí, 2=No** |
| 435 | _PA150R1 | 150+ minutos/semana | 1=Sí, 2=No |
| 436 | _PA300R1 | 300+ minutos/semana | 1=Sí, 2=No |
| 437 | _PA3002L | 300 minutos (2 niveles) | 1=Sí, 2=No |
| 438 | _PASTRNG | Cumple fortalecimiento | 1=Sí, 2=No |
| 439 | _PAREC | Cumple ambas guías | 1=Ambas, 2=Solo aeróbico, 3=Solo fuerza, 4=Ninguna |
| 440 | _PASTAER | Cumple ambas (2 niveles) | 1=Sí, 2=No |

### Variables de Seguridad y Vacunas (441-444)
| # | Variable | Descripción |
|---|----------|-------------|
| 441 | _RFSEAT2 | Siempre/casi siempre usa cinturón |
| 442 | _RFSEAT3 | Siempre usa cinturón |
| 443 | _FLSHOT5 | Adultos 65+ con vacuna gripe |
| 444 | _PNEUMO2 | Adultos 65+ con vacuna neumonía |

### **Variables de Alcohol (445-452)** ⭐
| # | Variable | Descripción | Valores |
|---|----------|-------------|---------|
| 445 | DRNKANY5 | Bebió en últimos 30 días | 1=Sí, 2=No |
| 446 | DROCDY3_ | Ocasiones de consumo/día | Calculado |
| 447 | **_RFBING5** | **Bebedor excesivo (binge)** | **1=No, 2=Sí** |
| 448 | _DRNKDY4 | Bebidas/día (bebedores) | Calculado |
| 449 | _DRNKMO4 | Bebidas/mes | Calculado |
| 450 | **_RFDRHV4** | **Bebedor de alto riesgo** | **1=No, 2=Sí** |
| 451 | _RFDRMN4 | Alto riesgo - hombres | 1=No, 2=Sí |
| 452 | _RFDRWM4 | Alto riesgo - mujeres | 1=No, 2=Sí |

### Variables de VIH (453-454)
| # | Variable | Descripción |
|---|----------|-------------|
| 453 | _AIDTST3 | Prueba de VIH alguna vez |
| 454 | HAVHPAD | Tiene dispositivo auditivo |

---

# VARIABLES CLAVE PARA TU PROYECTO (RESUMEN)

## Variables más útiles para análisis comparativo 2011 vs 2022:

### Estado de Salud
| Variable | Descripción |
|----------|-------------|
| GENHLTH | Salud general (1-5) |
| PHYSHLTH | Días mala salud física |
| MENTHLTH | Días mala salud mental |
| _RFHLTH | Buena salud (calculada) |

### Comportamientos
| Variable | Descripción |
|----------|-------------|
| _SMOKER3 / _RFSMOK3 | Fumador |
| _RFBING5 / _RFDRHV4 | Alcohol |
| _TOTINDA / _PACAT | Actividad física |
| SLEPTIME | Horas de sueño |
| _BMI5CAT / _RFBMI5 | IMC/Obesidad |

### Condiciones
| Variable | Descripción |
|----------|-------------|
| ADDEPEV2 | Depresión |
| DIABETE3 | Diabetes |
| _RFHYPE5 | Hipertensión |
| _RFCHOL | Colesterol alto |

### Demografía
| Variable | Descripción |
|----------|-------------|
| SEX | Sexo |
| _AGE_G / _AGE65YR | Edad |
| _EDUCAG | Educación |
| _INCOMG | Ingreso |
| _RACE_G | Raza |

---

*Total: 454 variables en BRFSS 2011*
*Documento para proyecto de Estadística - Universidad de La Habana, MATCOM*
