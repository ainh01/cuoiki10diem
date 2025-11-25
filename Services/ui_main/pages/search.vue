<script lang="ts" setup>
import { Comic } from 'types';

const comics = ref<Comic[]>([]);
const query = ref<string>('');
const isFetching = ref<boolean>(true);
const totalPages = ref<number>(1);
const currentPage = ref<number>(1);

const route = useRoute();
const router = useRouter();

const getSearchComics = async () => {
  try {
    isFetching.value = true;
    
    const endpoint = `/tim-kiem?keyword=${query.value}&page=${currentPage.value}`;
    const data = await useFetchData(endpoint);
    
    comics.value = data.data.items;
    totalPages.value = data?.total_pages;
    
  } catch (err) {
    console.error('Error fetching search results:', err);
  } finally {
    isFetching.value = false;
  }
};

query.value = route.query.keyword as string;
currentPage.value = route.query.page ? Number(route.query.page) : 1;
await getSearchComics();

const handleChangePage = (page: number) => {
  currentPage.value = page;
  router.replace({ query: { ...route.query, page } });
};

watch(route, async (newRoute) => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
  query.value = newRoute.query.keyword as string;
  currentPage.value = newRoute.query.page ? Number(newRoute.query.page) : 1;
  await getSearchComics();
});
</script>

<template>
  <Head>
    <Title>{{ `${query ? `${query} | STORIES` : 'STORIES'}` }}</Title>
    <Meta name="description" content="Free comic and manga reader online" />
  </Head>
  <main class="max-w-6xl mx-auto min-h-screen py-6 px-3">
    <div class="flex items-center flex-wrap gap-1 text-gray-500 font-bold text-lg">
      <NuxtLink to="/">Home</NuxtLink>
      <Icon name="icon-park:right" size="16" />
      <span>Kết quả tìm kiếm</span>
      <Icon name="icon-park:right" size="16" />
      <span class="text-black">{{ query }}</span>
    </div>

    <h4
      class="text-2xl text-center mt-8 font-bold text-gray-600"
      v-show="!isFetching && !comics.length"
    >
      No result
    </h4>

    <ul class="grid grid-cols-1 md:grid-cols-2 gap-6 py-5">
      <template v-if="isFetching">
        <li
          v-for="(_, idx) in new Array(8)"
          :key="idx"
          class="bg-gray-200 animate-pulse rounded-lg w-full h-44"
        ></li>
      </template>
      <template v-else>
        <NuxtLink
          :to="`/truyen-tranh/${comic.slug}`"
          v-for="comic in comics"
          :key="comic._id"
          class="flex flex-col sm:flex-row gap-4 rounded-lg border border-gray-100 bg-gray-50 p-4"
        >
          <img
            :src="'https://otruyenapi.com/uploads/comics/' + comic.thumb_url"
            :alt="comic.name"
            class="rounded aspect-[2/3] w-44 mx-auto sm:w-auto sm:h-36 border border-emerald-500 object-cover"
          />
          <div class="text-gray-500 font-bold w-full">
            <h3 class="text-lg text-black leading-5">
              {{ comic.name }}
            </h3>
            <p class="flex items-center gap-1 text-emerald-500">
              <template v-if="Array.isArray(comic.origin_name)">
                {{ comic.origin_name.join(' | ') }}
              </template>
              <template v-else-if="comic.origin_name === 'Updating'">
                <Icon name="mdi:dots-circle" size="16" />
                Updating
              </template>
              <template v-else>
                {{ comic.origin_name }}
              </template>
            </p>
            <ul class="text-sm flex items-center flex-wrap gap-2 mt-1">
              <li
                v-for="genre in comic.category"
                :key="genre.id"
                class="bg-cyan-100 text-cyan-800 text-xs px-2.5 py-0.5 rounded-full"
              >
                {{ genre.name }}
              </li>
            </ul>
          </div>
        </NuxtLink>
      </template>
    </ul>
  </main>
</template>
