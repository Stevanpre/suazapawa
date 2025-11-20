const fs = require('fs');
const path = require('path');

const paths = {
  cssSrc: path.join(__dirname, '..', 'web', 'static', 'css'),
  jsSrc: path.join(__dirname, '..', 'node_modules'),
  cssDest: "C:/Users/steva/OneDrive/Desktop/suazapawa/web/static/css",
  jsDest: "C:/Users/steva/OneDrive/Desktop/suazapawa/web/static/js"
};

// copiar un archivo
function copyFile(src, dest) {
  fs.copyFileSync(src, dest);
  console.log(`Copiado: ${dest}`);
}

// copiar carpeta completa recursivamente
function copyFolderRecursive(srcDir, destDir) {
  if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });

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

// copiar CSS generado
copyFolderRecursive(paths.cssSrc, paths.cssDest);

// copiar dependencias JS de node_modules (solo JS)
copyFolderRecursive(paths.jsSrc, paths.jsDest);
