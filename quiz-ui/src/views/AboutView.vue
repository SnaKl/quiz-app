<!-- General informations about the application -->
<template>
  <div class="about">
    <h1 class="my-5"><I18nTextComponent i18n-key="aboutPage" /></h1>
    <article>
      Quiz-App est une application développée par une équipe de trois étudiants
      jeunes et dynamiques. Passionés par l'informatique et plus
      particulièrement le développement web. En effet, ces trois têtes brûlées
      sont très friandes du PHP natif.
      <hr class="my-5" />
      <h3 class="mb-3">L'équipe</h3>
      <ul class="list-group w-25">
        <a
          class="list-group-item list-group-item-action align-items-center"
          href="https://github.com/Armadindon"
          target="_blank"
        >
          <img
            class="rounded me-2"
            src="https://github.com/Armadindon.png"
            alt="@Armadindon"
            width="32"
            height="32"
          />
          <span>
            <strong>Baptiste PERRIN</strong>
            @Armadindon
          </span>
        </a>
        <a
          class="list-group-item list-group-item-action align-items-center"
          href="https://github.com/SnakL"
          target="_blank"
        >
          <img
            class="rounded me-2"
            src="https://github.com/SnakL.png"
            alt="@SnakL"
            width="32"
            height="32"
          />
          <span>
            <strong>Colin LE PICHON</strong>
            @SnakL
          </span>
        </a>
        <a
          class="list-group-item list-group-item-action align-items-center"
          href="https://github.com/Mathouz"
          target="_blank"
        >
          <img
            class="rounded me-2"
            src="https://github.com/Mathouz.png"
            alt="@Mathouz"
            width="32"
            height="32"
          />
          <span>
            <strong>Mathieu PELLAN</strong>
            @Mathouz
          </span>
        </a>
      </ul>
      <hr class="my-5" />
      <h3>Demande de contact</h3>
      Nous n'acceptons malheureusement aucune demande de contact, merci de votre
      compréhension.
    </article>
  </div>
</template>

<script>
import I18nTextComponent from '../components/I18nTextComponent.vue';

export default {
  components: { I18nTextComponent }
};
</script>
