import { resolve } from 'path'
import { resolveFilesPath } from './utils'
const ROOT_PATH = resolve(__dirname, '../src')

export const createIssue = async (github, context, core) => {
  const filesPath = await resolveFilesPath(ROOT_PATH)
  // 一个题可能存在多个语言的解法，所以将数组转为对象
  const questionsMap = filesPath.reduce((map, filePath) => {
    const nameSplit = filePath.split('.')
    const questionName = `${nameSplit[0]}.${nameSplit[1]}`
    const suffix = nameSplit[1]
    if (map[questionName]) {
      const questions = map[questionName]
      questions.push({
        suffix,
        filePath
      })
    } else {
      map[questionName] = [
        {
          suffix,
          filePath
        }
      ]
    }
    return map
  }, {})
  console.log('questionsMap', questionsMap)
}
