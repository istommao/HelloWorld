import { defineConfig } from 'dumi';

export default defineConfig({
  themeConfig: {
    name: 'CodeMax',
    socialLinks: {
      github: "https://github.com/istommao/HelloWorld"
    },
    nav: [
      { title: 'Languages', link: '/langs' },
      { title: 'Database', link: '/database' },
      { title: 'Network', link: '/network' },
      { title: 'Practice', link: '/practice' },
    ],

  },
});
