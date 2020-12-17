import fs from 'fs'
import { promisify } from 'util'
import { join } from 'path'
const readDirPromise = promisify(fs.readdir)

export const resolveFilesPath = async (rootPath) => {
  if (fs.existsSync(rootPath)) {
    console.error(`${rootPath} is not a file or directory`)
  }
  let files = await readDirPromise(rootPath)
  return files.map((file) => join(rootPath, file))
}
