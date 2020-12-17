import * as core from '@actions/core'
import { context, getOctokit } from '@actions/github'
// import { createIssue } from './issue'

process.on('unhaandledRejection', errorHandler)
main().catch(errorHandler)

async function main() {
  const token = process.argv[2]
  const github = getOctokit(token)
  console.log('token', token)
  console.log('github', github)
  // await createIssue(github, context, core)
}

function errorHandler(err: any) {
  console.error(err)
  core.setFailed(`Unhandled error: ${err}`)
}
