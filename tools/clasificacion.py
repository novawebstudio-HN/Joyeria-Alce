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


# ── Segunda tanda (ZIP de septiembre) ────────────────────────────────────────
#
# Los originales de la primera tanda ya no estan en el repositorio, asi que esta
# tabla va por nombre de archivo: "<archivo> <tipo>/<linea> <material>". El id de
# cada pieza se calcula continuando la numeracion de su carpeta (ver BASE), asi
# que es reproducible sin depender del orden en que se lean los ZIP.

BASE = {
    ("anillos", "hombre"): 11,
    ("anillos", "mujer"): 62,
    ("aretes", "mujer"): 180,
    ("aretes", "ninos"): 2,
    ("collares", "hombre"): 3,
    ("collares", "mujer"): 32,
    ("collares", "ninos"): 1,
    ("esclavas", "hombre"): 19,
    ("esclavas", "mujer"): 16,
    ("esclavas", "ninos"): 4,
    ("juegos", "mujer"): 3,
    ("juegos", "ninos"): 1,
    ("pulseras", "mujer"): 19,
    ("tobilleras", "mujer"): 7,
}

NUEVAS = """
011f5756-7765-4cb2-a440-32929976561f.JPG collares/mujer plata
01a8665e-ad6f-4d79-b009-040374964c68.JPG collares/mujer plata
0227bdaf-ad66-44cb-93d1-d94e87544b07.JPG aretes/mujer plata
027af69b-e13b-4f43-a72d-1224d6d77a1f.JPG collares/mujer plata
02a21ae1-2e6b-4334-a6a0-fbb1ad4f695e.JPG esclavas/mujer plata
04c5812f-86cf-419f-98fb-84b8927d1d7a.JPG collares/mujer plata
04e39d5f-01a0-477c-905d-4edd8d9d5d80.JPG aretes/mujer plata
05785413-a288-4ee9-a6f2-5230ebfe6865.JPG aretes/mujer plata
05d6388c-2844-458a-9c2e-13932d36aef2.JPG collares/mujer plata
0766fff1-55bf-4519-901f-da8438fc4477.JPG aretes/mujer plata
07851353-172a-45cb-a659-792639fd1abc.JPG aretes/mujer plata
07d12c60-0e43-4a74-809e-b0be16dcae2e.JPG aretes/mujer plata
08995169-8459-4c62-b4b5-3ff295a0c214.JPG aretes/mujer plata
0947c79a-cb3a-4c7d-bd34-d60b9576bfe2.JPG aretes/mujer plata
09bbb118-1a95-4bb8-93c9-1816bb78c12e.JPG juegos/mujer plata
0a1318e7-76ea-4639-a541-3fd44be6a840.JPG juegos/mujer plata
0a7489f3-8d50-4522-b585-5a1e66e393bf.JPG pulseras/mujer plata
0b0f22ae-a436-4103-8f01-fa2804531a13.JPG pulseras/mujer plata
0b651988-abc5-450f-bba0-2663c8836600.JPG collares/mujer plata
0c39049c-3228-414d-90ad-d1f591de129f.JPG aretes/mujer plata
0c475b7e-14bd-4035-9389-76bda91293c1.JPG juegos/mujer plata
0cc99695-48d8-4269-af78-ed2e9d7ac1bf.JPG aretes/mujer plata
0d38d8e4-f85a-4675-ad5b-c9a5028e93d5.JPG collares/mujer plata
0f0c5aaf-a83e-4f61-83ee-52c93a78f018.JPG aretes/mujer plata
0f80d653-ac5e-4096-9f13-ad0b6789e614.JPG dijes/mujer plata
10c0da28-1fb1-471d-aaf6-6d3a2cc71aaf.JPG juegos/mujer plata
11cd53bb-ea0c-4ac6-b800-488ca22a70c4.JPG juegos/mujer plata
142efb2e-017c-48ae-95f4-e1d963e2a304.JPG aretes/mujer plata
14bc82c7-72e6-4e2a-a495-99257006ad1b.JPG juegos/mujer plata
154dcb17-ffd3-4229-9c08-693fb99206eb.JPG aretes/mujer plata
1b23bc35-f623-4bbe-8dbb-d3f97e4fa982.JPG pulseras/mujer plata
1b8f5e13-fa86-4ee3-8ce7-62e5b59240e6.JPG juegos/mujer plata
1bdf8a05-13c6-4635-98ee-c55746c64c54.JPG collares/mujer plata
1d0e04c9-5da0-4090-9c01-50b54e0870c8.JPG dijes/hombre plata
2269fd48-dd87-49c8-a34b-3f76aedd734a.JPG aretes/mujer plata
24403415-b419-4630-9a73-e2c4035a8d23.JPG juegos/mujer plata
24c0cf99-0bc7-403b-85a2-f80bb2279ee6.JPG juegos/mujer plata
24c7c750-afaf-4e3a-8c52-72443ff0fbdd.JPG aretes/mujer plata
26ecaab3-de5c-4623-b270-2a698930a15d.JPG juegos/mujer plata
2731c2bd-365b-4a30-a155-cec86dbc08f7.JPG juegos/mujer plata
27d7406e-edf8-475f-85ee-4dbe7118ff80.JPG aretes/mujer plata
2b8fc494-442c-4446-bbf9-0c0103a2e3db.JPG aretes/mujer plata
2cf6eeed-629b-413d-8c7d-ed0804e57f84.JPG pulseras/mujer plata
2ef5ed3c-3e02-4aca-b1e6-564b6a64a4ec.JPG juegos/mujer plata
304750d5-de48-4353-9fe6-d0d0cd99fe1b.JPG juegos/ninos plata
30914c07-78bb-42a8-b6db-99ecd5edfb3d.JPG juegos/mujer plata
3092af1a-0386-4259-99a0-400337e2b89d.JPG dijes/mujer plata
3397ca2e-3599-4262-9d20-39d32e2f9e6d.JPG aretes/mujer plata
33e9c6ef-1ac7-4fcf-8b43-7fab70190b15.JPG pulseras/mujer plata
35fc3fd3-b21e-42b7-bc92-ef15d66704bd.JPG aretes/mujer plata
361c8826-2ca8-42de-8f2f-a7fca01fa84c.JPG aretes/mujer plata
36f7072d-dde2-4eb2-8a70-15235a1a58cd.JPG aretes/mujer plata
37998cf6-6294-472a-85da-43008acbb3f3.JPG aretes/mujer plata
3a88796c-8ccb-4a58-a405-eb30906f0388.JPG aretes/mujer plata
3be08963-076a-419f-bd10-5034a44afa55.JPG pulseras/mujer plata
3cae08e1-25ff-4f51-ae3d-99b501ee4520.JPG aretes/mujer plata
3f4016bc-2ea3-4a2e-911d-d089a26926c0.JPG aretes/mujer plata
3f855a17-43d0-4d22-91b3-e0189ce24385.JPG aretes/mujer plata
3feafc12-d090-4c3e-a328-dcf976c2ead5.JPG aretes/mujer plata
4031cc1a-d693-40e8-8b46-379350c9403e.JPG collares/mujer plata
406180c8-66a2-4fe7-aa1f-fa2a7885912e.JPG aretes/mujer plata
40879c2a-8a6b-4215-bc72-b20a588f4d6c.JPG aretes/mujer plata
40d05bc3-eff2-4bdb-aa88-457daf50c358.JPG collares/mujer plata
41f30e24-16c2-4fa5-9c85-28b0eed9a713.JPG aretes/mujer plata
434ff26d-f16f-42fd-8771-2175eeb4d90a.JPG juegos/ninos plata
43598947-d295-4389-abf1-ba48f2f41f87.JPG collares/mujer plata
44d25441-cc7c-43e7-b334-d9376ad3a0f5.JPG aretes/mujer plata
454525f9-0707-4f70-b1ab-6a4cb27332b9.JPG juegos/mujer plata
47be3a41-781e-49eb-b15f-0cbd7101f29d.JPG aretes/mujer plata
4a89892b-ca58-4458-8362-f31094c264d3.JPG aretes/mujer plata
4aac8205-84b3-4eb0-95c8-2404abc85ec0.JPG juegos/mujer plata
4cbd827a-2651-413f-bf43-c0e0ba352c3c.JPG collares/mujer plata
4d10852f-0571-4985-bd1d-e6eee7274cae.JPG aretes/mujer plata
4ff578b3-1ca2-4fc0-91b7-a9abf58772d7.JPG dijes/ninos plata
502f43a3-54b9-4744-b3fc-e635ace0b5a2.JPG collares/mujer plata
5162cc79-5464-4d9a-af89-f2423b85726c.JPG aretes/mujer plata
5349e08b-e1bc-4db6-863e-4417565120f5.JPG juegos/mujer plata
5416724f-448d-43ef-9db1-66d7c93d7ca3.JPG collares/mujer plata
541f0100-b158-4f5e-8ce8-683786a2b3e5.JPG juegos/mujer plata
549af20c-9bb7-47d0-840d-49d48b2407f2.JPG aretes/mujer plata
57bbdb99-d021-419a-b27f-1b000f77d55f.JPG dijes/hombre plata
57f7ec11-012b-4bbd-a2f3-570aa276198c.JPG pulseras/mujer plata
57fc460a-b702-4aef-9c4c-ff383210afc2.JPG aretes/mujer plata
5977068b-d383-4cf1-8071-251c4fc8c993.JPG juegos/mujer plata
5a4eee90-6179-412a-b779-201218c071c4.JPG aretes/mujer plata
5ad6b2d1-712c-4bdb-b866-8a757b2d833d.JPG collares/mujer plata
5ce5de4b-7a2e-4e4e-ab67-62c62ee0f703.JPG aretes/mujer plata
5ead4691-2b33-4a88-9f1c-66829b78f210.JPG collares/mujer plata
5faa008b-ad8d-4127-b24f-4c0c1b6f8a35.JPG aretes/mujer plata
5ff9f45d-ab13-4b0a-a4cb-634a69a3399f.JPG collares/mujer plata
60656f4d-3f0b-4a7b-a697-4f3a1e5996e7.JPG esclavas/hombre plata
61266f5d-7eb1-419a-a9e8-4fe366647760.JPG aretes/mujer plata
64c838e6-863a-4586-acbf-e82c696d424a.JPG collares/mujer plata
677d297b-8d1e-4959-9602-2a1e73fd96fd.JPG aretes/mujer plata
69c5e989-1015-4a69-b5cd-e892d9673eb0.JPG aretes/mujer plata
6a9d870e-eecc-4797-9dc3-641eca14d5cf.JPG aretes/mujer plata
6aeec6b6-e5be-47b3-b0b9-63578c08c020.JPG esclavas/hombre plata
6d6c91cf-ce27-4384-913f-45b9f16ce991.JPG aretes/mujer plata
6d8163f0-94e1-4118-993b-ba5a9242a26a.JPG aretes/mujer plata
6e1d39c2-3444-46c8-84ac-a16ca10c6c3d.JPG juegos/mujer plata
6fdb44ec-e27a-430f-aedb-573c88b7a4c2.JPG juegos/mujer plata
7095b796-c0ef-4b09-b376-6751923e2e49.JPG pulseras/mujer plata
70bdbec0-2c59-4364-bf70-fa7b03fafa54.JPG esclavas/hombre plata
715b824e-84c2-4106-9d33-636f6e71afe2.JPG juegos/mujer plata
71c741e3-b187-4b32-8ca9-a3e619f6a212.JPG pulseras/mujer plata
71ef6182-9797-4043-a45c-c233eff82a22.JPG juegos/ninos plata
7341d7ba-17eb-4bc1-bdf0-2ac870f5413a.JPG pulseras/mujer plata
7530e011-70fa-4283-be83-23dfe874b873.JPG aretes/mujer plata
76001031-bb70-4c20-a3d9-d30288220a0c.JPG collares/mujer plata
76c82c85-e0fb-4dce-8ee7-fa3fb2e3fce1.JPG aretes/mujer plata
77362ffb-c704-4653-854b-626f9028bb30.JPG aretes/mujer plata
78ad16cf-cf25-451b-812d-689bb3ed4e58.JPG dijes/mujer plata
795a636b-8aa9-4398-b60a-dbbc6cab686b.JPG juegos/mujer plata
79e29a23-959c-4a11-9894-9bad221773dc.JPG aretes/mujer plata
7a62d09e-0c76-4863-a289-66ccc540dec6.JPG aretes/mujer plata
7a829985-c988-4ea7-a63b-7be76cf302d4.JPG collares/mujer plata
7ab4e206-d01a-449e-936a-bf44e10aa9da.JPG aretes/mujer plata
7c348e8d-0eac-4170-9f6c-6d81c142e0a3.JPG juegos/mujer plata
7c8a1997-012d-4d02-b201-80aaa63907b6.JPG collares/mujer plata
7c96f3ee-62a0-44e5-aa7a-eb763b53276a.JPG aretes/mujer plata
7d320b06-d134-43ac-86fe-db3cc4317bc4.JPG pulseras/mujer plata
7d6fcf7f-b3d3-41e5-b9eb-be37fa80a05b.JPG aretes/mujer plata
7e11a162-2b77-4f88-bf0e-c477490236e8.JPG aretes/mujer plata
811b756a-b0f1-4c79-9f3c-ebceb5d168de.JPG juegos/mujer plata
81eac895-8f42-46d7-bc22-e49063bf004d.JPG aretes/mujer plata
81eb44fa-cfad-47ea-a70f-dbb0fa4a813f.JPG aretes/mujer plata
83dbd917-23b8-424b-9bca-68df3ce1afd3.JPG esclavas/mujer plata
84524abf-75e4-4e82-809f-2dd63734c567.JPG aretes/mujer plata
87e76aff-8d0a-4384-b1a8-42eff1296e2c.JPG juegos/mujer plata
8abf5993-eaca-4be3-af11-e149f49313e0.JPG aretes/mujer plata
8b1bbe4c-2c7b-4e40-a228-a1dcc1db1db4.JPG dijes/mujer plata
8dc6c586-c2a7-484e-a924-4b13bdc9c13a.JPG juegos/mujer plata
8f91f384-42a5-4729-8cdc-3e5ea6f7d9cc.JPG collares/mujer plata
8ff1d397-ba9c-40ab-a06f-631bfc42a599.JPG juegos/ninos plata
9010fdc5-9801-417a-b34d-3cec43d706ed.JPG aretes/mujer plata
91d1e2b6-1e75-4bec-a7cd-9e85d2bc7489.JPG aretes/mujer plata
9366e858-b66a-49d7-ab4b-fd595344103e.JPG aretes/mujer plata
93f8c03f-3d39-48d1-8ed2-956458beae15.JPG juegos/mujer plata
94c62a66-9710-43d6-83b2-c09a10f85de8.JPG aretes/mujer plata
95e9bfc4-84c0-484b-a948-41a19b3789ed.JPG collares/mujer plata
95f0ee0f-5b2b-4225-9aae-59b012fc6b98.JPG juegos/mujer plata
9621543d-87e2-44aa-9784-25522cd9e45c.JPG juegos/mujer plata
98a7b0ad-86dc-47b5-82b6-27290cce8621.JPG aretes/mujer plata
99de2325-1ac7-4d30-9570-28a682ad2a3f.JPG aretes/mujer plata
9dce5bc9-ecbd-4eb1-8d42-d052bcdbd891.JPG juegos/mujer plata
9ddf63d0-b52c-487d-a5d9-2366fb8bd29f 2.JPG aretes/mujer plata
9e38afc3-d311-4731-935f-587cc19322f8.JPG aretes/mujer plata
9f7100ba-db7f-4852-8329-0afbe5948d99.JPG aretes/mujer plata
a0105f8b-705f-4bd5-a4c4-7ae2118f1c5c.JPG aretes/mujer plata
a0d69fd3-8a3b-49ac-9e1a-95a88c6b49fd.JPG aretes/mujer plata
a1b3e494-b37f-4979-a3c0-134e817909cf.JPG juegos/mujer plata
a60af88b-1cfb-4cb6-92cc-780b74b49b90.JPG aretes/mujer plata
a7f9f8ea-e236-4b7a-88df-025081df317e.JPG aretes/mujer plata
ab000ac7-ef78-4c1f-8338-19202103d0ab.JPG aretes/mujer plata
abeb4c01-16bf-4d00-81a1-6e60c2ba055d.JPG aretes/mujer plata
ad553751-2e56-4c17-b49f-e3e922075647.JPG pulseras/mujer plata
af26e786-eb56-41b1-ac5a-1afa10985b6e.JPG juegos/mujer plata
af9c1790-23d9-4571-bf71-6291df405f9b.JPG pulseras/mujer plata
afca75d9-1a81-4844-8485-83cedcdd6da1.JPG aretes/mujer plata
b1fbe9f2-6c93-4b4f-9b42-f7047a2068b8.JPG juegos/mujer plata
b20ac08c-db62-45dd-b8ae-b1f87ba84079.JPG juegos/mujer plata
b27306f4-8bb8-4b0a-b889-7e0c4b6b531e.JPG aretes/mujer plata
b3a82757-84a5-4c52-90e3-7e43c153508e.JPG aretes/mujer plata
b6a88d07-e331-424d-8eae-20c395944192.JPG aretes/mujer plata
b6f218dd-8584-41f1-90d1-e970e17bed3c.JPG aretes/mujer plata
b7581466-718b-4014-aa44-4572464c65d7.JPG juegos/mujer plata
bbc3a44c-a46a-4735-b15c-086909e118d2.JPG esclavas/hombre plata
c04cbe7f-d162-4e16-9a00-8f089a380d4c.JPG pulseras/mujer plata
c099c11d-f3a5-462f-b871-74caeaec2c74.JPG collares/mujer plata
c296b931-10e8-4011-8314-947849a3c0a2.JPG aretes/mujer plata
c3609c3f-cf66-4ae7-b0b1-34d69f794705.JPG aretes/mujer plata
c45674c1-eb4a-4d6b-ae21-9a2660b4d14e.JPG juegos/mujer plata
c5228e63-ecda-4035-9d75-6af73eca2e2d.JPG juegos/mujer plata
c5957b1d-712f-450f-9d4f-dfbaab623a8e.JPG aretes/mujer plata
c5d03cb6-0e06-4bcb-9591-8a9faffae113.JPG collares/mujer plata
c5f68976-1af5-4125-84b0-733fc3a0659b.JPG aretes/mujer plata
c843cdf1-b1d8-4358-9620-d473b7d750fb.JPG collares/mujer plata
cc57f5d2-d1f9-4789-8ac5-43587cd766b7.JPG aretes/mujer plata
ced5f0c7-9fbc-4527-98ac-0172384a8104.JPG dijes/ninos plata
d09bc44d-9062-4c4e-94ea-aef940311d83.JPG tobilleras/mujer plata
d133497e-21ae-446b-a0af-a4a2e0e8aded.JPG tobilleras/mujer plata
d37cdc7c-91cc-4c49-8eac-a36b93f105a7.JPG tobilleras/mujer plata
d4ca5607-2ca6-45c7-80eb-df18cfd00f4e.JPG pulseras/mujer plata
d540cd27-1e80-4bb9-adc2-06d9003e94ad.JPG aretes/mujer plata
d65dae02-0cd9-42f2-83b0-22cd795db4ed.JPG pulseras/mujer plata
daa3e4aa-d491-4d4f-b0b5-4f325219288b.JPG esclavas/mujer plata
dbc2d5f3-9e6b-4af9-adfd-1ae4872bad40.JPG aretes/mujer plata
dc3059ee-b376-4de6-b93e-90d125f86632.JPG aretes/mujer plata
dc744af1-3b17-4f7f-bce9-6d50bf463a07.JPG aretes/mujer plata
dd9707fb-b8b4-4a70-a4ee-f34a29dc2557.JPG aretes/mujer plata
deb04322-9e79-4e30-bc58-cfe069e849cc.JPG aretes/mujer plata
dfaf1ede-9296-42c7-a265-db4596de16a4.JPG aretes/mujer plata
e12de37c-b75f-4261-a16d-f197f5525686.JPG aretes/mujer plata
e4bfde21-fc3f-4124-af26-ec9332c39443.JPG esclavas/hombre plata
e7b4f49f-3418-4665-8139-acc3044d2cd1.JPG aretes/mujer plata
e8600383-1a7c-44eb-8322-b2a3332efcb7.JPG dijes/mujer plata
e9301567-6a5f-4ba3-9c63-d6ee8d523acf.JPG juegos/mujer plata
e9ca9031-b4fa-40ef-8a9b-eac4aa4d80d3.JPG juegos/mujer plata
ea46cd47-3acd-48fe-b56d-9a0572a856a9.JPG juegos/mujer plata
ea8a2723-e4fd-4e34-a0d4-55ed87abf08a.JPG juegos/mujer plata
eaedd1b8-47da-405f-9d6d-2fdb78e0a512.JPG dijes/mujer plata
ee0ff977-b1fe-4027-bd41-6b718ec314d2.JPG juegos/mujer plata
eea7df7f-7942-4031-990f-e7f19d188aaa.JPG juegos/mujer plata
f04af929-af0e-4083-9715-44c6ee031a16.JPG aretes/mujer plata
f09c47a1-8c9f-46ea-bffc-c4ab93bff081.JPG juegos/mujer plata
f7853e72-48b2-4724-b1d4-5f7a6e05739e.JPG juegos/mujer plata
f80b3dbd-0d7d-44f6-bd65-c5b7187e8f4b.JPG aretes/mujer plata
f9de46ac-a1e2-4e3b-b3c1-8f0de1ded2ce.JPG pulseras/mujer plata
fa6bded7-0971-42f9-b97d-d699bd62f3a6.JPG aretes/mujer plata
fd34d706-01c1-4796-8a2b-c895598b17cb.JPG juegos/mujer plata
fff7db89-a5fa-4a35-8372-a432debd0834.JPG dijes/hombre plata
"""


def cargar_nuevas():
    """Devuelve {archivo: (tipo, genero, material, id)} para la segunda tanda."""
    # rsplit: algun nombre de archivo trae espacios ("... 2.JPG").
    filas = [l.rsplit(" ", 2) for l in NUEVAS.strip().splitlines()]
    filas.sort(key=lambda f: f[0])
    contadores = dict(BASE)
    asignadas = {}
    for archivo, ruta, material in filas:
        tipo, genero = ruta.split("/")
        contadores[(tipo, genero)] = contadores.get((tipo, genero), 0) + 1
        pid = f"{tipo}-{genero}-{contadores[(tipo, genero)]:03d}"
        asignadas[archivo] = (tipo, genero, material, pid)
    return asignadas


def materiales_por_id():
    """Material de cada pieza del catalogo completo, por identificador."""
    mapa = {pid: "plata" for pid in cargar_materiales()}
    for _, _, material, pid in cargar_nuevas().values():
        mapa[pid] = material
    return mapa
