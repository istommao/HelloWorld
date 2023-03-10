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
      { title: 'Algo', link: '/algo' },
      { title: 'Practice', link: '/practice' },
      { title: 'Daily', link: '/daily_report' },
    ],

  },
});
