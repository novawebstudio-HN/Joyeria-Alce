/* Joyería Alce — catálogo
   Dos vistas: inicio (colecciones) y colección (piezas de un tipo, con
   filtros de material y línea). La ruta vive en el hash: #/aretes?m=plata */

(() => {
  'use strict';

  const $ = (sel) => document.querySelector(sel);

  const vistaInicio = $('#vista-inicio');
  const vistaColeccion = $('#vista-coleccion');
  const menu = $('#menu');
  const colecciones = $('#colecciones');
  const atajos = $('#atajos');
  const rejilla = $('#rejilla');
  const vacio = $('#vacio');
  const centinela = $('#centinela');
  const selMaterial = $('#sel-material');
  const selLinea = $('#sel-linea');
  const campoMaterial = $('#campo-material');
  const campoLinea = $('#campo-linea');
  const btnQuitar = $('#quitar');

  const visor = $('#visor');
  const visorImg = $('#visor-img');

  const POR_TANDA = 40;
  const TODO = 'todo';

  let datos = null;
  let nombreTipo = {};
  let nombreGenero = {};
  let nombreMaterial = {};
  let ruta = { tipo: TODO, material: TODO, linea: TODO };
  let visibles = [];
  let mezclaMateriales = false;
  let dibujadas = 0;
  let actual = 0;
  let ultimoFoco = null;

  /* ── Arranque ─────────────────────────────────────── */

  const cabecera = document.querySelector('.cabecera');
  const medirCabecera = () =>
    document.documentElement.style.setProperty('--alto-cabecera', `${cabecera.offsetHeight}px`);
  medirCabecera();
  new ResizeObserver(medirCabecera).observe(cabecera);

  fetch('data/catalogo.json')
    .then((r) => {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    })
    .then((d) => {
      datos = d;
      d.tipos.forEach((t) => { nombreTipo[t.slug] = t.nombre; });
      d.generos.forEach((g) => { nombreGenero[g.slug] = g.nombre; });
      d.materiales.forEach((m) => { nombreMaterial[m.slug] = m.nombre; });
      montarMenu();
      montarInicio();
      window.addEventListener('hashchange', navegar);
      navegar();
    })
    .catch(() => {
      vacio.textContent = 'No se pudo cargar el catálogo. Recarga la página.';
      vacio.hidden = false;
    });

  const piezasDe = (tipo) =>
    tipo === TODO ? datos.piezas : datos.piezas.filter((p) => p.tipo === tipo);

  /* ── Inicio ───────────────────────────────────────── */

  function montarMenu() {
    const enlaces = [{ slug: TODO, nombre: 'Todo' }].concat(
      datos.tipos.filter((t) => piezasDe(t.slug).length));
    menu.replaceChildren(...enlaces.map((t) => {
      const a = document.createElement('a');
      a.href = `#/${t.slug}`;
      a.textContent = t.nombre;
      a.dataset.tipo = t.slug;
      return a;
    }));
  }

  function montarInicio() {
    colecciones.replaceChildren(...datos.tipos
      .map((t) => ({ t, piezas: piezasDe(t.slug) }))
      .filter(({ piezas }) => piezas.length)
      .map(({ t, piezas }) => {
        const portada = piezas.find((p) => p.id === t.portada) || piezas[0];
        const a = document.createElement('a');
        a.className = 'tarjeta';
        a.href = `#/${t.slug}`;
        a.innerHTML = `
          <img class="tarjeta__foto" src="${portada.thumb}" alt="" width="${portada.w}"
               height="${portada.h}" loading="lazy" decoding="async">
          <span class="tarjeta__pie">
            <span class="tarjeta__nombre">${t.nombre}</span>
            <span class="tarjeta__n">${piezas.length}</span>
          </span>`;
        return a;
      }));

    const cuenta = (clave, valor) => datos.piezas.filter((p) => p[clave] === valor).length;
    const enlaces = datos.materiales
      .map((m) => ({ href: `#/${TODO}?m=${m.slug}`, nombre: m.nombre, n: cuenta('material', m.slug) }))
      .concat(datos.generos
        .map((g) => ({ href: `#/${TODO}?l=${g.slug}`, nombre: g.nombre, n: cuenta('genero', g.slug) })))
      .filter((e) => e.n);

    atajos.replaceChildren(...enlaces.map((e) => {
      const a = document.createElement('a');
      a.className = 'atajo';
      a.href = e.href;
      a.innerHTML = `${e.nombre} <span>${e.n}</span>`;
      return a;
    }));
  }

  /* ── Rutas ────────────────────────────────────────── */

  function leerRuta() {
    const bruto = location.hash.replace(/^#\/?/, '');
    const [camino, consulta] = bruto.split('?');
    const params = new URLSearchParams(consulta || '');
    const tipo = datos.tipos.some((t) => t.slug === camino) ? camino : (camino === TODO ? TODO : '');
    const valido = (valor, lista) => (lista.some((x) => x.slug === valor) ? valor : TODO);
    return {
      tipo,
      material: valido(params.get('m'), datos.materiales),
      linea: valido(params.get('l'), datos.generos),
    };
  }

  function escribirRuta({ tipo, material, linea }, reemplazar) {
    const params = new URLSearchParams();
    if (material !== TODO) params.set('m', material);
    if (linea !== TODO) params.set('l', linea);
    const cadena = params.toString();
    const destino = `#/${tipo}${cadena ? `?${cadena}` : ''}`;
    if (location.hash === destino) return;
    if (reemplazar) history.replaceState(null, '', destino);
    else location.hash = destino;
  }

  function navegar() {
    ruta = leerRuta();
    const enColeccion = ruta.tipo !== '';

    vistaInicio.hidden = enColeccion;
    vistaColeccion.hidden = !enColeccion;
    menu.querySelectorAll('a').forEach((a) => {
      if (a.dataset.tipo === ruta.tipo) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });

    if (enColeccion) mostrarColeccion();
    window.scrollTo({ top: 0 });
  }

  /* ── Colección ────────────────────────────────────── */

  function opciones(select, lista, valor) {
    select.replaceChildren(...lista.map((o) => {
      const op = document.createElement('option');
      op.value = o.slug;
      op.textContent = o.n === undefined ? o.nombre : `${o.nombre} (${o.n})`;
      if (o.slug === valor) op.selected = true;
      return op;
    }));
  }

  function mostrarColeccion() {
    const delTipo = piezasDe(ruta.tipo);
    $('#col-titulo').textContent = ruta.tipo === TODO ? 'Todo el catálogo' : nombreTipo[ruta.tipo];

    // Cada selector ofrece solo lo que existe dentro de la colección y cuenta ya
    // con el otro filtro aplicado; si no hay más de una opción, no aparece.
    const disponibles = (clave, lista, otros) => lista
      .map((o) => ({ ...o, n: delTipo.filter((p) => p[clave] === o.slug && otros(p)).length }))
      .filter((o) => o.n);

    const porLinea = (p) => ruta.linea === TODO || p.genero === ruta.linea;
    const porMaterial = (p) => ruta.material === TODO || p.material === ruta.material;
    const materiales = disponibles('material', datos.materiales, porLinea);
    const lineas = disponibles('genero', datos.generos, porMaterial);

    campoMaterial.hidden = materiales.length < 2;
    campoLinea.hidden = lineas.length < 2;
    if (campoMaterial.hidden) ruta.material = TODO;
    if (campoLinea.hidden) ruta.linea = TODO;

    const totalMaterial = delTipo.filter(porLinea).length;
    const totalLinea = delTipo.filter(porMaterial).length;
    opciones(selMaterial, [{ slug: TODO, nombre: 'Todos', n: totalMaterial }].concat(materiales), ruta.material);
    opciones(selLinea, [{ slug: TODO, nombre: 'Todas', n: totalLinea }].concat(lineas), ruta.linea);
    btnQuitar.hidden = ruta.material === TODO && ruta.linea === TODO;

    visibles = delTipo.filter((p) =>
      (ruta.material === TODO || p.material === ruta.material) &&
      (ruta.linea === TODO || p.genero === ruta.linea));

    const partes = [`${visibles.length} ${visibles.length === 1 ? 'pieza' : 'piezas'}`];
    if (ruta.material !== TODO) partes.push(nombreMaterial[ruta.material]);
    if (ruta.linea !== TODO) partes.push(nombreGenero[ruta.linea]);
    $('#col-conteo').textContent = partes.join(' · ');

    mezclaMateriales = new Set(visibles.map((p) => p.material)).size > 1;

    rejilla.replaceChildren();
    dibujadas = 0;
    vacio.hidden = visibles.length > 0;
    dibujarTanda();
  }

  selMaterial.addEventListener('change', () => {
    escribirRuta({ ...ruta, material: selMaterial.value });
  });
  selLinea.addEventListener('change', () => {
    escribirRuta({ ...ruta, linea: selLinea.value });
  });
  btnQuitar.addEventListener('click', () => {
    escribirRuta({ tipo: ruta.tipo, material: TODO, linea: TODO });
  });

  function dibujarTanda() {
    const hasta = Math.min(dibujadas + POR_TANDA, visibles.length);
    const frag = document.createDocumentFragment();

    for (let i = dibujadas; i < hasta; i++) {
      const p = visibles[i];
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'pieza';
      b.dataset.indice = String(i);
      b.setAttribute('aria-label', `Ampliar pieza ${i + 1} de ${visibles.length}`);

      const img = document.createElement('img');
      img.src = p.thumb;
      img.alt = '';
      img.width = p.w;
      img.height = p.h;
      img.loading = i < 8 ? 'eager' : 'lazy';
      img.decoding = 'async';
      img.dataset.cargando = '1';
      const listo = () => delete img.dataset.cargando;
      if (img.complete) listo();
      else img.addEventListener('load', listo, { once: true });

      b.appendChild(img);
      if (mezclaMateriales) {
        const pie = document.createElement('span');
        pie.className = 'pieza__material';
        pie.textContent = nombreMaterial[p.material];
        b.appendChild(pie);
      }
      frag.appendChild(b);
    }

    rejilla.appendChild(frag);
    dibujadas = hasta;
  }

  rejilla.addEventListener('click', (e) => {
    const pieza = e.target.closest('.pieza');
    if (pieza) abrirVisor(Number(pieza.dataset.indice), pieza);
  });

  new IntersectionObserver((entradas) => {
    if (entradas.some((en) => en.isIntersecting) && dibujadas < visibles.length) dibujarTanda();
  }, { rootMargin: '900px 0px' }).observe(centinela);

  /* ── Visor ────────────────────────────────────────── */

  function abrirVisor(indice, origen) {
    ultimoFoco = origen || null;
    actual = indice;
    visor.hidden = false;
    document.body.classList.add('sin-scroll');
    mostrar();
    $('#visor-cerrar').focus();
  }

  function cerrarVisor() {
    visor.hidden = true;
    visorImg.removeAttribute('src');
    document.body.classList.remove('sin-scroll');
    if (ultimoFoco) ultimoFoco.focus();
  }

  function mover(paso) {
    if (!visibles.length) return;
    actual = (actual + paso + visibles.length) % visibles.length;
    mostrar();
  }

  function mostrar() {
    const p = visibles[actual];
    visorImg.src = p.full;
    visorImg.alt = `Pieza ${actual + 1} de ${visibles.length}`;
    $('#visor-etiqueta').textContent = `${nombreTipo[p.tipo]} · ${nombreMaterial[p.material]}`;
    $('#visor-conteo').textContent = `${actual + 1} / ${visibles.length}`;
    // Precarga de la siguiente y la anterior para que el paso sea inmediato.
    [1, -1].forEach((d) => {
      const v = visibles[(actual + d + visibles.length) % visibles.length];
      if (v) new Image().src = v.full;
    });
  }

  $('#visor-cerrar').addEventListener('click', cerrarVisor);
  $('#visor-prev').addEventListener('click', () => mover(-1));
  $('#visor-sig').addEventListener('click', () => mover(1));
  visor.addEventListener('click', (e) => {
    if (!e.target.closest('.visor__btn') && e.target !== visorImg) cerrarVisor();
  });

  document.addEventListener('keydown', (e) => {
    if (visor.hidden) return;
    if (e.key === 'Escape') cerrarVisor();
    else if (e.key === 'ArrowRight') mover(1);
    else if (e.key === 'ArrowLeft') mover(-1);
  });

  let x0 = null, y0 = null;
  visor.addEventListener('touchstart', (e) => {
    x0 = e.changedTouches[0].clientX;
    y0 = e.changedTouches[0].clientY;
  }, { passive: true });
  visor.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    const dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) mover(dx < 0 ? 1 : -1);
    x0 = y0 = null;
  }, { passive: true });
})();
