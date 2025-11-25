<script lang="ts" setup>
import { meta } from '@/utils/data';

const extractComicsData = (response: any) => {
  if (!response) return [];
  if (response.items && Array.isArray(response.items)) {
    return response.items;
  }
  if (response.data?.items && Array.isArray(response.data.items)) {
    return response.data.items;
  }
  if (Array.isArray(response)) {
    return response;
  }
  return [];
};

// Fetch all data with error handling
const [
  homeClientResponse,
  ancientComicsResponse,
  actionComicsResponse,
  adultComicsResponse,
  adventureComicsResponse,
  animeComicsResponse,
  reincarnationComicsResponse,
] = await Promise.all([
  useFetchData('/home_client').catch(() => null),
  useFetchData('/the-loai/co-dai').catch(() => null),
  useFetchData('/the-loai/action').catch(() => null),
  useFetchData('/the-loai/adult').catch(() => null),
  useFetchData('/the-loai/adventure').catch(() => null),
  useFetchData('/the-loai/anime').catch(() => null),
  useFetchData('/the-loai/chuyen-sinh').catch(() => null),
]);

// Extract comic data safely
const homeClientComics = extractComicsData(homeClientResponse);
const ancientComics = extractComicsData(ancientComicsResponse);
const actionComics = extractComicsData(actionComicsResponse);
const adultComics = extractComicsData(adultComicsResponse);
const adventureComics = extractComicsData(adventureComicsResponse);
const animeComics = extractComicsData(animeComicsResponse);
const reincarnationComics = extractComicsData(reincarnationComicsResponse);

useSeoMeta(meta());
useServerSeoMeta(meta());
</script>

<template>
  <main class="max-w-6xl mx-auto py-5 px-3">
    <Swiper
      :slides-per-view="6"
      :loop="true"
      :space-between="10"
      :autoplay="{
        delay: 5000,
        disableOnInteraction: false,
      }"
      :modules="[SwiperAutoplay]"
      :breakpoints="{
        0: {
          slidesPerView: 1,
        },
        320: {
          slidesPerView: 2,
        },
        576: {
          slidesPerView: 3,
        },
        768: {
          slidesPerView: 4,
        },
        1024: {
          slidesPerView: 5,
        },
        1280: {
          slidesPerView: 6,
        },
      }"
    >
      <SwiperSlide v-for="comic in adventureComics" :key="comic._id">
        <ComicCard :comic="comic" :detail="false" />
      </SwiperSlide>
    </Swiper>
    
    <ComicsSlide
      title="Cổ Đại"
      :comics="ancientComics"
      icon=""
      link="/the-loai/co-dai"
    />
    <ComicsSlide
      title="Action"
      :comics="actionComics"
      icon=""
      link="/the-loai/action"
    />
    <ComicsSlide
      title="Trưởng thành"
      :comics="adultComics"
      icon=""
      link="/the-loai/adult"
    />
    <ComicsSlide
      title="Phiêu lưu"
      :comics="adventureComics"
      icon=""
      link="/the-loai/adventure"
    />
    <ComicsSlide
      title="Truyện Anime"
      :comics="animeComics"
      icon=""
      link="/the-loai/anime"
    />
    <ComicsSlide
      title="Chuyển sinh"
      :comics="reincarnationComics"
      icon=""
      link="/the-loai/chuyen-sinh"
    />
  </main>
</template>