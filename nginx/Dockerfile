# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ysaito <ysaito@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/27 21:17:56 by ysaito            #+#    #+#              #
#    Updated: 2021/11/27 23:45:12 by ysaito           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM    debian:buster

RUN     apt-get update && apt-get -y upgrade \ 
        && apt-get -y install \ 
            nginx \ 
            vim

CMD     ["/usr/sbin/nginx", "-g", "daemon off;"]
