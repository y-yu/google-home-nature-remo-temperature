Google Home + Nature Remoで室温を取得するサーバーアプリ
=========================================================

## Document

- https://qiita.com/yyu/items/41d398e1abfe1fb51d8d

## How to use

1. `git clone https://github.com/y-yu/google-home-nature-remo-temperature.git`
2. `cd google-home-nature-remo-temperature`
3. `heroku login`
    * もしCLIの`heroku`がない場合はHomebrewなどで適宜インストールする
4. `heroku container:login`
5. `heroku container:push web -a 《App name》`
6. `heroku container:release web -a 《App name》`
