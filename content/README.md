本项目基于 Vue3 + Vite + TypeScript 构建。请确保您的开发环境满足以下要求：
- **Node.js**: v18 或更高版本 ([下载链接](https://nodejs.org/en/download))
- **pnpm**: 推荐使用 pnpm 作为包管理工具 ([安装指南](https://pnpm.io/installation))

在项目根目录下运行以下命令以安装所需的依赖包：

```shell
pnpm install
```

安装完成后，运行以下命令启动本地开发服务器：

```shell
pnpm run dev
```

启动成功后，您可以在浏览器中访问 `http://localhost:5173/` 查看项目。

如果需要将项目构建为生产环境版本，请运行：

```shell
pnpm run build
```

构建完成后的文件将存放在 `dist` 目录下。您也可以使用以下命令预览构建后的产物：

```shell
pnpm run preview
```

项目所需的数据文件已预处理并放置在 `public/data/` 目录下，前端在运行时会按需加载这些数据文件。
