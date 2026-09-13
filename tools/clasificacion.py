# Clasificacion manual de cada imagen original (indice -> "tipo/genero").
# El indice corresponde al orden alfabetico de:
#   sorted("Joyeria Alce 2"/*.JPG) + sorted("Joyeria Alce"/*.JPG)
CLASIFICACION = """
0 collares/mujer
1 pulseras/mujer
2 aretes/mujer
3 anillos/mujer
4 anillos/mujer
5 anillos/mujer
6 aretes/mujer
7 aretes/mujer
8 collares/mujer
9 aretes/mujer
10 aretes/mujer
11 collares/hombre
12 aretes/mujer
13 aretes/mujer
14 aretes/mujer
15 esclavas/mujer
16 aretes/mujer
17 tobilleras/mujer
18 anillos/mujer
19 collares/mujer
20 aretes/mujer
21 esclavas/mujer
22 anillos/mujer
23 aretes/mujer
24 esclavas/mujer
25 aretes/mujer
26 anillos/mujer
27 aretes/mujer
28 aretes/mujer
29 aretes/mujer
30 aretes/mujer
31 aretes/mujer
32 aretes/mujer
33 aretes/mujer
34 aretes/mujer
35 aretes/mujer
36 aretes/mujer
37 aretes/mujer
38 aretes/mujer
39 aretes/mujer
40 aretes/mujer
41 aretes/mujer
42 anillos/mujer
43 anillos/mujer
44 anillos/mujer
45 anillos/mujer
46 esclavas/mujer
47 anillos/mujer
48 anillos/mujer
49 collares/mujer
50 aretes/mujer
51 aretes/mujer
52 tobilleras/mujer
53 aretes/mujer
54 aretes/mujer
55 aretes/mujer
56 anillos/mujer
57 pulseras/mujer
58 aretes/mujer
59 esclavas/mujer
60 anillos/mujer
61 pulseras/mujer
62 esclavas/hombre
63 aretes/mujer
64 aretes/mujer
65 aretes/mujer
66 esclavas/hombre
67 aretes/mujer
68 aretes/mujer
69 anillos/mujer
70 anillos/mujer
71 collares/mujer
72 anillos/mujer
73 esclavas/hombre
74 aretes/mujer
75 aretes/mujer
76 collares/mujer
77 anillos/mujer
78 aretes/mujer
79 anillos/hombre
80 anillos/mujer
81 aretes/mujer
82 aretes/mujer
83 aretes/mujer
84 aretes/mujer
85 aretes/mujer
86 esclavas/ninos
87 collares/mujer
88 aretes/mujer
89 aretes/mujer
90 aretes/mujer
91 esclavas/mujer
92 esclavas/hombre
93 aretes/mujer
94 anillos/hombre
95 anillos/mujer
96 aretes/mujer
97 collares/mujer
98 aretes/mujer
99 aretes/mujer
100 aretes/mujer
101 aretes/mujer
102 juegos/mujer
103 anillos/mujer
104 esclavas/hombre
105 anillos/hombre
106 anillos/mujer
107 aretes/mujer
108 aretes/mujer
109 aretes/mujer
110 anillos/hombre
111 aretes/mujer
112 aretes/mujer
113 aretes/mujer
114 esclavas/hombre
115 aretes/mujer
116 aretes/mujer
117 pulseras/mujer
118 aretes/mujer
119 aretes/mujer
120 anillos/mujer
121 aretes/mujer
122 collares/mujer
123 aretes/mujer
124 aretes/mujer
125 anillos/mujer
126 collares/ninos
127 aretes/mujer
128 esclavas/hombre
129 aretes/mujer
130 aretes/mujer
131 pulseras/mujer
132 pulseras/mujer
133 aretes/mujer
134 aretes/mujer
135 aretes/mujer
136 aretes/mujer
137 anillos/mujer
138 aretes/mujer
139 esclavas/mujer
140 aretes/mujer
141 anillos/mujer
142 aretes/mujer
143 aretes/mujer
144 aretes/mujer
145 esclavas/hombre
146 collares/hombre
147 collares/mujer
148 aretes/mujer
149 anillos/mujer
150 collares/mujer
151 anillos/mujer
152 juegos/ninos
153 aretes/mujer
154 esclavas/mujer
155 aretes/ninos
156 aretes/mujer
157 anillos/hombre
158 aretes/mujer
159 esclavas/mujer
160 collares/mujer
161 anillos/hombre
162 aretes/mujer
163 pulseras/mujer
164 aretes/mujer
165 collares/mujer
166 pulseras/mujer
167 anillos/mujer
168 aretes/mujer
169 anillos/mujer
170 anillos/mujer
171 aretes/mujer
172 aretes/mujer
173 anillos/mujer
174 collares/mujer
175 aretes/mujer
176 collares/mujer
177 aretes/mujer
178 collares/mujer
179 anillos/mujer
180 aretes/mujer
181 esclavas/hombre
182 aretes/mujer
183 aretes/mujer
184 anillos/mujer
185 esclavas/hombre
186 anillos/mujer
187 anillos/mujer
188 aretes/mujer
189 anillos/hombre
190 esclavas/hombre
191 collares/mujer
192 anillos/hombre
193 collares/mujer
194 tobilleras/mujer
195 anillos/mujer
196 esclavas/mujer
197 aretes/mujer
198 aretes/mujer
199 aretes/mujer
200 anillos/mujer
201 aretes/mujer
202 aretes/mujer
203 collares/mujer
204 aretes/mujer
205 anillos/mujer
206 aretes/mujer
207 aretes/mujer
208 aretes/mujer
209 aretes/mujer
210 aretes/mujer
211 tobilleras/mujer
212 anillos/mujer
213 aretes/mujer
214 aretes/mujer
215 collares/mujer
216 aretes/mujer
217 aretes/mujer
218 collares/mujer
219 aretes/mujer
220 aretes/ninos
221 aretes/mujer
222 aretes/mujer
223 aretes/mujer
224 esclavas/mujer
225 anillos/hombre
226 aretes/mujer
227 aretes/mujer
228 aretes/mujer
229 aretes/mujer
230 collares/mujer
231 pulseras/mujer
232 esclavas/mujer
233 anillos/mujer
234 esclavas/hombre
235 aretes/mujer
236 aretes/mujer
237 aretes/mujer
238 pulseras/mujer
239 esclavas/hombre
240 anillos/mujer
241 aretes/mujer
242 aretes/mujer
243 aretes/mujer
244 collares/mujer
245 tobilleras/mujer
246 collares/mujer
247 aretes/mujer
248 aretes/mujer
249 aretes/mujer
250 anillos/mujer
251 pulseras/mujer
252 anillos/mujer
253 esclavas/ninos
254 tobilleras/mujer
255 aretes/mujer
256 aretes/mujer
257 aretes/mujer
258 anillos/mujer
259 anillos/mujer
260 esclavas/ninos
261 esclavas/hombre
262 juegos/mujer
263 juegos/mujer
264 aretes/mujer
265 esclavas/ninos
266 aretes/mujer
267 pulseras/mujer
268 anillos/hombre
269 aretes/mujer
270 anillos/mujer
271 esclavas/hombre
272 esclavas/mujer
273 aretes/mujer
274 aretes/mujer
275 aretes/mujer
276 aretes/mujer
277 anillos/mujer
278 anillos/mujer
279 aretes/mujer
280 aretes/mujer
281 anillos/mujer
282 aretes/mujer
283 aretes/mujer
284 aretes/mujer
285 aretes/mujer
286 collares/mujer
287 aretes/mujer
288 aretes/mujer
289 aretes/mujer
290 anillos/mujer
291 esclavas/mujer
292 aretes/mujer
293 aretes/mujer
294 anillos/mujer
295 aretes/mujer
296 anillos/mujer
297 aretes/mujer
298 aretes/mujer
299 esclavas/hombre
300 collares/mujer
301 aretes/mujer
302 aretes/mujer
303 aretes/mujer
304 pulseras/mujer
305 anillos/mujer
306 aretes/mujer
307 pulseras/mujer
308 anillos/mujer
309 collares/mujer
310 aretes/mujer
311 aretes/mujer
312 aretes/mujer
313 pulseras/mujer
314 aretes/mujer
315 aretes/mujer
316 aretes/mujer
317 pulseras/mujer
318 collares/mujer
319 aretes/mujer
320 collares/mujer
321 aretes/mujer
322 aretes/mujer
323 collares/mujer
324 esclavas/hombre
325 aretes/mujer
326 aretes/mujer
327 anillos/mujer
328 aretes/mujer
329 pulseras/mujer
330 esclavas/mujer
331 aretes/mujer
332 anillos/mujer
333 aretes/mujer
334 aretes/mujer
335 aretes/mujer
336 aretes/mujer
337 esclavas/hombre
338 collares/mujer
339 collares/hombre
340 pulseras/mujer
341 collares/mujer
342 anillos/mujer
343 esclavas/hombre
344 anillos/mujer
345 anillos/mujer
346 anillos/mujer
347 aretes/mujer
348 aretes/mujer
349 anillos/hombre
350 aretes/mujer
351 aretes/mujer
352 aretes/mujer
353 aretes/mujer
354 aretes/mujer
355 tobilleras/mujer
356 aretes/mujer
357 pulseras/mujer
358 esclavas/mujer
359 anillos/mujer
"""

def cargar():
    mapa = {}
    for linea in CLASIFICACION.strip().splitlines():
        idx, ruta = linea.split()
        tipo, genero = ruta.split("/")
        mapa[int(idx)] = (tipo, genero)
    return mapa


# Material de cada pieza, leido de la propia foto ("Oro 10K", "plata italy 925",
# "PLATA FINA"). La mayoria del catalogo es oro 10K, asi que aqui solo se listan
# las piezas de la linea de plata 925; el resto se toma como oro.
PLATA = """
anillos-hombre-001  anillos-mujer-002  anillos-mujer-009
anillos-mujer-013  anillos-mujer-016  anillos-mujer-017
anillos-mujer-019  anillos-mujer-020  anillos-mujer-022
anillos-mujer-029  anillos-mujer-032  anillos-mujer-037
anillos-mujer-038  anillos-mujer-039  anillos-mujer-042
anillos-mujer-043  anillos-mujer-046  anillos-mujer-049
anillos-mujer-053  anillos-mujer-055  anillos-mujer-056
anillos-mujer-057  aretes-mujer-002  aretes-mujer-004
aretes-mujer-005  aretes-mujer-006  aretes-mujer-007
aretes-mujer-010  aretes-mujer-015  aretes-mujer-016
aretes-mujer-018  aretes-mujer-019  aretes-mujer-020
aretes-mujer-021  aretes-mujer-024  aretes-mujer-027
aretes-mujer-028  aretes-mujer-030  aretes-mujer-031
aretes-mujer-032  aretes-mujer-035  aretes-mujer-036
aretes-mujer-037  aretes-mujer-038  aretes-mujer-039
aretes-mujer-040  aretes-mujer-042  aretes-mujer-044
aretes-mujer-045  aretes-mujer-046  aretes-mujer-048
aretes-mujer-049  aretes-mujer-052  aretes-mujer-053
aretes-mujer-054  aretes-mujer-055  aretes-mujer-057
aretes-mujer-060  aretes-mujer-061  aretes-mujer-062
aretes-mujer-064  aretes-mujer-065  aretes-mujer-067
aretes-mujer-069  aretes-mujer-070  aretes-mujer-073
aretes-mujer-075  aretes-mujer-076  aretes-mujer-077
aretes-mujer-078  aretes-mujer-079  aretes-mujer-081
aretes-mujer-083  aretes-mujer-084  aretes-mujer-085
aretes-mujer-086  aretes-mujer-088  aretes-mujer-091
aretes-mujer-092  aretes-mujer-093  aretes-mujer-094
aretes-mujer-095  aretes-mujer-097  aretes-mujer-098
aretes-mujer-099  aretes-mujer-100  aretes-mujer-101
aretes-mujer-102  aretes-mujer-103  aretes-mujer-104
aretes-mujer-105  aretes-mujer-106  aretes-mujer-107
aretes-mujer-108  aretes-mujer-109  aretes-mujer-115
aretes-mujer-116  aretes-mujer-117  aretes-mujer-118
aretes-mujer-119  aretes-mujer-121  aretes-mujer-122
aretes-mujer-123  aretes-mujer-124  aretes-mujer-125
aretes-mujer-126  aretes-mujer-127  aretes-mujer-128
aretes-mujer-131  aretes-mujer-132  aretes-mujer-134
aretes-mujer-135  aretes-mujer-136  aretes-mujer-137
aretes-mujer-140  aretes-mujer-141  aretes-mujer-142
aretes-mujer-143  aretes-mujer-144  aretes-mujer-145
aretes-mujer-147  aretes-mujer-148  aretes-mujer-149
aretes-mujer-150  aretes-mujer-151  aretes-mujer-152
aretes-mujer-154  aretes-mujer-155  aretes-mujer-157
aretes-mujer-159  aretes-mujer-161  aretes-mujer-163
aretes-mujer-164  aretes-mujer-165  aretes-mujer-166
aretes-mujer-167  aretes-mujer-170  aretes-mujer-176
aretes-mujer-178  collares-mujer-001  collares-mujer-002
collares-mujer-005  collares-mujer-009  collares-mujer-011
collares-mujer-015  collares-mujer-026  collares-mujer-027
collares-mujer-032  pulseras-mujer-004  pulseras-mujer-007
pulseras-mujer-011  pulseras-mujer-013  pulseras-mujer-015
pulseras-mujer-017  pulseras-mujer-019
"""


def cargar_materiales():
    """Devuelve el conjunto de identificadores de piezas de plata 925."""
    return set(PLATA.split())
