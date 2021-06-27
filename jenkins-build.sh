# Jenkins build script

rm -rf dist/

npm install

npm run generate

rsync -av ./dist/ /path/to/host/directory

# Small hack to make nginx work with the build

mkdir /path/to/host/directory/<nginx location name>

# Will need to add other assets/build folders/files down the line
cp -R static/ img/ *.js /path/to/host/directory/<nginx location name>