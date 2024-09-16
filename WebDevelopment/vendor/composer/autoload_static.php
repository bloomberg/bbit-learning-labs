<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit0a036f78667e977ad31b3b36b78abbbd
{
    public static $prefixLengthsPsr4 = array (
        'C' => 
        array (
            'Composer\\Installers\\' => 20,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Composer\\Installers\\' => 
        array (
            0 => __DIR__ . '/..' . '/composer/installers/src/Composer/Installers',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit0a036f78667e977ad31b3b36b78abbbd::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit0a036f78667e977ad31b3b36b78abbbd::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit0a036f78667e977ad31b3b36b78abbbd::$classMap;

        }, null, ClassLoader::class);
    }
}