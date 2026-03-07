const fs = require('fs');
const path = require('path');

// Directorios base
const root = path.join(__dirname, '..');
const staticRoot = path.join(root, 'web', 'static');

const paths = {
  cssSrc: path.join(staticRoot, 'css'), // CSS ya generado por tailwind
  cssDest: path.join(staticRoot, 'css'),
  vendorDest: path.join(staticRoot, 'vendor') // Nuevo destino para librerías externas
};

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

// copiar un archivo
function copyFile(src, dest) {
  ensureDir(path.dirname(dest));
  fs.copyFileSync(src, dest);
  console.log(`Copiado: ${dest}`);
}

// copiar carpeta completa recursivamente
function copyFolderRecursive(srcDir, destDir) {
  if (!fs.existsSync(srcDir)) return;
  ensureDir(destDir);
  fs.readdirSync(srcDir).forEach(file => {
    const srcPath = path.join(srcDir, file);
    const destPath = path.join(destDir, file);
    if (fs.lstatSync(srcPath).isDirectory()) {
      copyFolderRecursive(srcPath, destPath);
    } else {
      copyFile(srcPath, destPath);
    }
  });
}

// Copiar Tailwind generado (mantener comportamiento previo)
copyFolderRecursive(paths.cssSrc, paths.cssDest);

// Paquetes a copiar de forma selectiva desde node_modules
const pkgRoot = path.join(root, 'node_modules');

const packages = [
  {
    name: 'flowbite',
    items: [
      { type: 'file', src: ['dist', 'flowbite.min.js'], dest: ['flowbite', 'dist', 'flowbite.min.js'] },
      { type: 'file', src: ['dist', 'flowbite.min.css'], dest: ['flowbite', 'dist', 'flowbite.min.css'] }
    ]
  },
  {
    name: 'aos',
    items: [
      { type: 'file', src: ['dist', 'aos.js'], dest: ['aos', 'dist', 'aos.js'] },
      { type: 'file', src: ['dist', 'aos.css'], dest: ['aos', 'dist', 'aos.css'] }
    ]
  },
  {
    name: '@fortawesome', // fontawesome scoped package
    subName: 'fontawesome-free',
    items: [
      // Copiamos css + webfonts manteniendo estructura relativa para que las fuentes carguen
      { type: 'file', src: ['css', 'all.min.css'], dest: ['fontawesome', 'css', 'all.min.css'] },
      { type: 'folder', src: ['webfonts'], dest: ['fontawesome', 'webfonts'] }
    ]
  },
  {
    name: 'alpinejs',
    items: [
      { type: 'file', src: ['dist', 'cdn.min.js'], dest: ['alpinejs', 'cdn.min.js'] }
    ]
  },
  {
    name: 'vanilla-tilt',
    items: [
      { type: 'file', src: ['dist', 'vanilla-tilt.min.js'], dest: ['vanilla-tilt', 'vanilla-tilt.min.js'] }
    ]
  }
];

function copyPackages() {
  ensureDir(paths.vendorDest);
  packages.forEach(pkg => {
    const base = pkg.subName ? path.join(pkgRoot, pkg.name, pkg.subName) : path.join(pkgRoot, pkg.name);
    if (!fs.existsSync(base)) {
      console.warn(`Paquete no encontrado, omitiendo: ${pkg.subName || pkg.name}`);
      return;
    }
    pkg.items.forEach(item => {
      const srcPath = path.join(base, ...item.src);
      const destPath = path.join(paths.vendorDest, ...item.dest);
      if (item.type === 'file') {
        if (fs.existsSync(srcPath)) copyFile(srcPath, destPath); else console.warn(`Archivo no existe: ${srcPath}`);
      } else if (item.type === 'folder') {
        copyFolderRecursive(srcPath, destPath);
      }
    });
  });
}

copyPackages();
