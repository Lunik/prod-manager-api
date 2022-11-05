# Project Info

All sources are located inside the `prodmanager` folder.

## Key Technical Skills

- [Requests][requests]

## Directories

- `docs`: Library documentation
- `tests`: Unitaries tests
- `prodmanager`: Sources of the library

## Can I create a merge request ?

Yes, you can.

Also, please don't rush or ask for ETA, because I have to understand the merge request, make sure it is no breaking changes and stick to my vision of this project, especially for large merge requests.

I will mark your merge request in the [milestones][gitlab-milestones], if I am plan to review and merge it.

✅ Accept:
- Bug/Security fix

⚠️ Discussion required
- New features
- Large merge requests

❌ Won't Merge
- Do not pass auto test
- Any breaking changes
- Duplicated merge request
- Buggy
- Existing logic is completely modified or deleted for no reason


### Recommended Merge Request Guideline

Before deep into coding, discussion first is preferred. Creating an empty merge request for discussion would be recommended.

1. Fork the project
2. Clone your fork repo to local
3. Create a new branch
4. Create an empty commit
   `git commit -m "[empty commit] merge request for <YOUR TASK NAME>" --allow-empty`
5. Push to your fork repo
6. [Create a merge request][gitlab-new-mr]
7. Write a proper description
8. Click "Change to draft"
9. Engage a discussion

## Project Styles

I personally do not like something need to learn so much and need to config so much before you can finally start the app.

- Easy to install for non-Docker users, no native build dependency is needed (at least for x86_64), no extra config, no extra effort to get it run
- Single container for Docker users, no very complex docker-compose file. Just map the volume and expose the port, then good to go
- Easy to use
- The web UI styling should be consistent and nice.

## Coding Styles

- 2 spaces indentation

## Name convention

- Function and methods : underscore_type
- Classes : PascalCaseType

## Tools

- Python >= 3.7
- Git

## Install dependencies

```bash
poetry install
```

## Unit Test

Test are made using [pytest][pytest] framework and run with :

```bash
python3 -m pytest \
  -v \
  -n 4 \
  --cov="prodmanager" \
  --junitxml=result.xml \
  --html=report.html \
  tests/

coverage html
```

## Release Procedures

1. Update the `CHANGELOG.md` file
2. Update the `pyproject.toml` file
2. Merge from `develop` branch to `master`
4. Tag the latest commit of the `master` branch with the version number
5. Wait for [CI/CD pipeline][gitlab-pipeline-tag] to succeed
6. Create a Release from the GitLab UI containing the content of the `CHANGELOG.md` file

<!-- Links -->

[requests]: https://requests.readthedocs.io
[pytest]: https://pytest.org

[gitlab-milestones]: https://gitlab.com/prod-manager/prod-manager/-/milestones
[gitlab-new-mr]: https://gitlab.com/prod-manager/prod-manager/-/merge_requests/new?merge_request%5Btarget_branch%5D=develop
[gitlab-pipeline-tag]: https://gitlab.com/prod-manager/prod-manager/-/pipelines?scope=tags
