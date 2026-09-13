/* Joyería Alce — catálogo
   Carga data/catalogo.json, arma la rejilla, filtra por tipo y línea,
   y abre el visor a pantalla completa. */

(() => {
  'use strict';

  const $ = (sel) => document.querySelector(sel);

  const rejilla = $('#rejilla');
  const conteo = $('#conteo');
  const vacio = $('#vacio');
  const centinela = $('#centinela');
  const filtroTipo = $('#filtro-tipo');
  const filtroGenero = $('#filtro-genero');

  const visor = $('#visor');
  const visorImg = $('#visor-img');
  const visorPie = $('#visor-pie');

  const POR_TANDA = 40;

  let piezas = [];
  let visibles = [];
  let dibujadas = 0;
  let actual = 0;
  let ultimoFoco = null;
  let filtros = { tipo: 'todo', genero: 'todo' };

  /* ── Arranque ─────────────────────────────────────── */

  // La barra de filtros se pega justo debajo de la cabecera, sea cual sea su alto.
  const cabecera = document.querySelector('.cabecera');
  const medirCabecera = () => {
    document.documentElement.style.setProperty('--alto-cabecera', `${cabecera.offsetHeight}px`);
  };
  medirCabecera();
  new ResizeObserver(medirCabecera).observe(cabecera);


  fetch('data/catalogo.json')
    .then((r) => {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    })
    .then((datos) => {
      piezas = datos.piezas;
      montarFiltros(datos);
      leerHash();
      aplicarFiltros();
    })
    .catch(() => {
      conteo.textContent = '';
      vacio.textContent = 'No se pudo cargar el catálogo. Recarga la página.';
      vacio.hidden = false;
    });

  /* ── Filtros ──────────────────────────────────────── */

  function montarFiltros(datos) {
    const cuenta = (clave, valor) => piezas.filter((p) => p[clave] === valor).length;

    const tipos = [{ slug: 'todo', nombre: 'Todo', n: piezas.length }].concat(
      datos.tipos
        .map((t) => ({ slug: t.slug, nombre: t.nombre, n: cuenta('tipo', t.slug) }))
        .filter((t) => t.n > 0)
    );
    const generos = [{ slug: 'todo', nombre: 'Todas las líneas', n: null }].concat(
      datos.generos
        .map((g) => ({ slug: g.slug, nombre: g.nombre, n: cuenta('genero', g.slug) }))
        .filter((g) => g.n > 0)
    );

    tipos.forEach((t) => filtroTipo.appendChild(chip(t, 'tipo')));
    generos.forEach((g) => filtroGenero.appendChild(chip(g, 'genero')));
    pintarChips();
  }

  function chip(item, grupo) {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'chip';
    b.dataset.grupo = grupo;
    b.dataset.valor = item.slug;
    b.setAttribute('aria-pressed', 'false');
    b.innerHTML = item.n === null
      ? item.nombre
      : `${item.nombre}<span class="chip__n">${item.n}</span>`;
    b.addEventListener('click', () => {
      filtros[grupo] = item.slug;
      pintarChips();
      escribirHash();
      aplicarFiltros();
      const alto = cabecera.offsetHeight + document.getElementById('filtros').offsetHeight;
      const tope = document.getElementById('galeria').offsetTop - alto - 8;
      if (window.scrollY > tope) window.scrollTo({ top: tope, behavior: 'smooth' });
    });
    return b;
  }

  function pintarChips() {
    document.querySelectorAll('.chip').forEach((c) => {
      c.setAttribute('aria-pressed', String(filtros[c.dataset.grupo] === c.dataset.valor));
    });
  }

  function aplicarFiltros() {
    visibles = piezas.filter((p) =>
      (filtros.tipo === 'todo' || p.tipo === filtros.tipo) &&
      (filtros.genero === 'todo' || p.genero === filtros.genero));

    rejilla.replaceChildren();
    dibujadas = 0;
    vacio.hidden = visibles.length > 0;
    conteo.textContent = visibles.length === 1
      ? '1 pieza'
      : `${visibles.length} piezas`;
    dibujarTanda();
  }

  /* ── Rejilla ──────────────────────────────────────── */

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
      img.complete ? listo() : img.addEventListener('load', listo, { once: true });

      b.appendChild(img);
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
    visorPie.textContent = `${actual + 1} / ${visibles.length}`;
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

  // Deslizar en móvil.
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

  /* ── Hash (permite compartir un filtro) ───────────── */

  function escribirHash() {
    const partes = [];
    if (filtros.tipo !== 'todo') partes.push(filtros.tipo);
    if (filtros.genero !== 'todo') partes.push(filtros.genero);
    const nuevo = partes.length ? `#${partes.join('-')}` : ' ';
    history.replaceState(null, '', nuevo === ' ' ? location.pathname : nuevo);
  }

  function leerHash() {
    const h = location.hash.replace('#', '');
    if (!h) return;
    const tipos = new Set(piezas.map((p) => p.tipo));
    const generos = new Set(piezas.map((p) => p.genero));
    h.split('-').forEach((parte) => {
      if (tipos.has(parte)) filtros.tipo = parte;
      else if (generos.has(parte)) filtros.genero = parte;
    });
    pintarChips();
  }
})();
