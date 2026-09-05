import { execFileSync } from 'node:child_process'
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { basename, dirname, extname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const projectRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const assetDir = join(projectRoot, 'marketing', 'assets')
const sources = [
  'xhs-cover.svg',
  'xhs-workflow.svg',
  'xhs-proof.svg',
  'xhs-export.svg',
  'xhs-pricing.svg',
  'goofish-card.svg',
  'douyin-cover.svg'
]
const renderDir = mkdtempSync(join(tmpdir(), 'haobushou-social-'))

function embedRasterImages(svgSource, svgPath) {
  return svgSource.replace(/xlink:href="([^"]+\.png)"/g, (_, relativePath) => {
    const imagePath = resolve(dirname(svgPath), relativePath)
    const encoded = readFileSync(imagePath).toString('base64')
    return `xlink:href="data:image/png;base64,${encoded}"`
  })
}

try {
  for (const source of sources) {
    const sourcePath = join(assetDir, source)
    const embeddedPath = join(renderDir, source)
    const outputPath = join(assetDir, `${basename(source, extname(source))}.png`)
    const embedded = embedRasterImages(readFileSync(sourcePath, 'utf8'), sourcePath)

    writeFileSync(embeddedPath, embedded)
    execFileSync('/usr/bin/sips', ['-s', 'format', 'png', embeddedPath, '--out', outputPath], {
      stdio: 'inherit'
    })
  }
} finally {
  rmSync(renderDir, { recursive: true, force: true })
}
